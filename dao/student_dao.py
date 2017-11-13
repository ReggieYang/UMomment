import json
from sqlalchemy import *
import datetime

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  # No logging
metadata = MetaData(db)

student = Table('student', metadata, autoload=True)
followership = Table('followership', metadata, autoload=True)
membership = Table('membership', metadata, autoload=True)
circle = Table('circle', metadata, autoload=True)
moment = Table('moment', metadata, autoload=True)
likingmoment = Table('likingmoment', metadata, autoload=True)
momentcomment = Table('momentcomment', metadata, autoload=True)
trend = Table('trend', metadata, autoload=True)
likingtrend = Table('likingtrend', metadata, autoload=True)
trendcomment = Table('trendcomment', metadata, autoload=True)
school = Table('school', metadata, autoload=True)


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


def multirow2listdict(row):
    list = []
    for rs in row:
        dict = {}
        for key in rs.keys():
            dict[key] = rs[key]
        list.append(dict)
    return list


def create_student(info):
    statement = "INSERT INTO student ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
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
        statement += quotevalue(info[key])
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
    statement += str(followerid)
    statement += " and followed_id="
    statement += str(followedid)
    db.execute(statement)
    return


def find_student_by_nickname(nickname):
    result = student.select(student.c.nick_name == nickname)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    s = {}
    s['user_id']=rs.user_id
    return s

# def find_my_followings(userid):
#     followingid = followership.select(followership.c.follower_id==userid).alias("follwingid")
#     result = student.select(student.c.user_id==followingid.c.followered)




def join_circle(userid, circleid, sincetime):
    i = membership.insert()
    i.execute(member_id=userid, circle_id=circleid, since=sincetime)
    return


def find_circle(circleid):
    result = circle.select(circle.c.circle_id == circleid)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    s = row2dict(rs)
    return s


# return all the pairs of school id and school name
def find_all_schools():
    school = Table('school', metadata, autoload=True)
    s = school.select()
    rs = s.execute()
    d = multirow2listdict(rs)
    return d


# info = {'moment_id':55, 'author_id': 5, 'content': 'yeah', 'time':'2017-10-09 19:28:30.824310'}
def insert_moment(info):
    statement = "INSERT INTO moment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


# info = {'user_id':9, 'moment_id':41, 'time':'2017-10-09 19:42:43.579866'}
def like_moment(info):
    statement = "INSERT INTO likingmoment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def unlike_moment(userid, momentid):
    statement = "DELETE FROM likingmoment WHERE user_id="
    statement += str(userid)
    statement += " and moment_id="
    statement += str(momentid)
    db.execute(statement)
    return


# info = {'comment_id':12,'author_id':9,'to_user':1,'moment_id':55,'content':'yyyy','time':'2017-10-09 21:38:44.677678'}
def comment_moment(info):
    statement = "INSERT INTO momentcomment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


# info = {'trend_id':11, 'author_id':4, 'circle_id':2, 'content':'yyyy', 'time':'2017-10-09 21:47:31.127708'}
def post_trend(info):
    statement = "INSERT INTO trend ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def like_trend(info):
    statement = "INSERT INTO likingtrend ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def unlike_trend(userid, trendid):
    statement = "DELETE FROM likingtrend WHERE user_id="
    statement += str(userid)
    statement += " and trend_id="
    statement += str(trendid)
    db.execute(statement)
    return


# info = {'comment_id': 13, 'author_id': 6, 'trend_id': 11, 'content': 'nnnn', 'time': '2017-10-09 21:47:31.127708'}
def comment_trend(info):
    statement = "INSERT INTO trendcomment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return
