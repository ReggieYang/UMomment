import json
from dao.student_dao import find_student, update_student


def login(student_id, password):
    student = find_student(student_id)

    if student['password'] == password:
        return student
    else:
        return None


def get_student_l(user_id):
    return find_student(user_id)


def update_student_l(student):
    user_id = student['user_id']
    student.pop('user_id', None)
    update_student(user_id, student)


def follow(user_id, following_id):
    return


def unfollow(user_id, following_id):
    return
