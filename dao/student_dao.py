import json
from sqlalchemy import *
import datetime

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  #No logging
metadata = MetaData(db)
def create(student):
    return


def find(id):
    student = Table('student', metadata, autoload=True)
    result = student.select(student.c.user_id == id)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    return rs


def update(student):
    return


def follow(student, follow):
    return


def unfollow(student, follow):
    return
