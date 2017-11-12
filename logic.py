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
    # need a select on several tables, similar to what we wrote in the first part --- one of those 3 sql
    return [{"author_id": "1", "like": 0, "moment_id": 123, "like_count": 123, "author_name": "Reggie",
             "content": "Philadelphia center Joel Embiid has agreed to a five-year, $148 million designated rookie scale max extension, league sources told ESPN.",
             "image": "", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"author_id": "2", "content": "this outfit", "like": 1, "moment_id": 12, "like_count": 3,
             "image": "https://pbs.twimg.com/media/DOUFsExV4AE2WyL.jpg:large", "author_name": "Xfl",
             "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]


def like_moment_l(moment_id, user_id):
    # print(str(user_id) + 'like' + str(moment_id))
    return 122


def unlike_moment_l(moment_id, user_id):
    # print(str(user_id) + 'unlike' + str(moment_id))
    return 25


def comment_moment_l(comment):
    print(str(comment))
    return


def get_comment_momment_l(moment_id):
    return [{"author_name": "ReggieYang", "to_user": "Xfl", "content": "Hello", "author_id": 3,
             "time": datetime.datetime.now().strftime("%Y-%m-%d")},
            {"author_name": "Naruhodou", "to_user": "Mitsurugi", "content": "Hi", "author_id": 123,
             "time": datetime.datetime.now().strftime("%Y-%m-%d")},
            {"author_name": "Naruto", "to_user": "Sasuke", "content": "Haha", "author_id": 769,
             "time": "2017-06-05"}]
