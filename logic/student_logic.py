import json

from dao.student_dao import find
from vo import Student




def login(student_id, password):
    student = find(id)

    if student['password'] == password:
        return student
    else:
        return None
