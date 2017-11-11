import json
from sqlalchemy import *
import datetime

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  # No logging
metadata = MetaData(db)

student = Table('student', metadata, autoload=True)
followership = Table('followership', metadata, autoload=True)

def quotevalue(value):
    statement = ''
    if type(value) == type('a'):
        statement += "'"
    statement += str(value)
    if type(value) == type('a'):
        statement += "'"
    return statement

def row2dict(row):
    d = {}
    for rs in row.keys():
        d[rs] = row[rs]
    return d


def create_student(info):
    statement = "INSERT INTO student ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    # i = student.insert()
    # i.execute(user_id=s['user_id'], nick_name=s['nick_name'], avatar=s['avatar'], school_id=s['school_id'],
    #           since=s['since'], email=s['email'], password=s['password'],
    #           introduction=s['introduction'])
    return


def find_student(id):
    result = student.select(student.c.user_id == id)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    # s = {'user_id': rs.user_id, 'nick_name': rs.nick_name, 'avatar': rs.avatar, 'school_id': rs.school_id,
    #      'since': rs.since, 'email': rs.email, 'password': rs.password, 'introduction': rs.introduction}
    s = row2dict(rs)
    return s


# All the info about update
def update_student(id, info):
    statement = "UPDATE student SET "
    for key in info:
        statement += key
        statement += '='
        quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ' WHERE user_id='
    statement += str(id)
    db.execute(statement)
    return


def follow(followerid, followedid, sincetime):
    i = followership.insert()
    i.execute(follower_id=followerid, followed_id=followedid, since=sincetime)
    return


def unfollow(followerid, followedid):
    statement = "DELETE FROM followership WHERE follower_id="
    statement += followerid
    statement += " and followed_id="
    statement += followedid
    db.execute(statement)
    return
