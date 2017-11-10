import json
from sqlalchemy import *
import datetime

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  # No logging
metadata = MetaData(db)


def row2dict(row):
    d = {}
    for rs in row.keys():
        d[rs] = row[rs]
    return d


def create(student):
    return


def find(id):
    student = Table('student', metadata, autoload=True)
    result = student.select(student.c.user_id == id)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    # s = {'user_id': rs.user_id, 'nick_name': rs.nick_name, 'avatar': rs.avatar, 'school_id': rs.school_id,
    #      'since': rs.since, 'email': rs.email, 'password': rs.password, 'introduction': rs.introduction}
    s = row2dict(rs)
    return s


def update(student):
    return


def follow(student, follow):
    return


def unfollow(student, follow):
    return
