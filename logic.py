import json

import datetime

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


def get_my_moment(user_id):
    return [{"author_id": "1", "like": 0, "moment_id": 123, "like_count": 123,
             "content": "Philadelphia center Joel Embiid has agreed to a five-year, $148 million designated rookie scale max extension, league sources told ESPN.",
             "image": "", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"author_id": "2", "content": "this outfit", "like": 1, "moment_id": 12, "like_count": 3,
             "image": "https://pbs.twimg.com/media/DOUFsExV4AE2WyL.jpg:large",
             "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]


def like_moment_l(moment_id, user_id):
    # print(str(user_id) + 'like' + str(moment_id))
    return 122


def unlike_moment_l(moment_id, user_id):
    # print(str(user_id) + 'unlike' + str(moment_id))
    return 25
