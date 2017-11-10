import json

from dao.student_dao import find
from vo import Student


def login(student_id, password):
    student = find(student_id)

    if student['password'] == password:
        return student
    else:
        return None


def update_student(student):
    return


def follow(user_id, following_id):
    return


def unfollow(user_id, following_id):
    return
