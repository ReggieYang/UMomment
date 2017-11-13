import json

import datetime

from dao.student_dao import find_student, update_student


def login(student_id, password):
    student = find_student(student_id)

    if student['password'] == password:
        return student
    else:
        return None


def get_schools_l():
    schools = ["Columbia", "NJU", "NFLS", "Yale"]
    d = []
    for i in range(0, len(schools)):
        d.append({"school_id": i, "school_name": schools[i]})
    return d


def get_student_l(user_id):
    return find_student(user_id)


def create_student_l(student):
    print(str(student))
    student['user_id'] = 17
    student['password'] = "bbrownlau"
    student['since'] = datetime.datetime.now()
    return student


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


def get_my_trend_l(user_id):
    content1 = "Philadelphia center Joel Embiid has agreed to a five-year, $148 million " \
               "designated rookie scale max extension, league sources told ESPN."
    content2 = "The Golden State Warriors are making life difficult for more than just " \
               "their NBA contemporaries."
    # need a select on several tables, similar to what we wrote in the first part --- one of those 3 sql
    return [{"author_id": "1", "like": 0, "trend_id": 123, "like_count": 123, "author_name": "Reggie",
             "content": content1[0:50], "circle_id": 12, "circle_name": "NBA",
             "image": "", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"author_id": "2", "content": content2[0:50], "like": 1, "trend_id": 12, "like_count": 3,
             "image": "https://pbs.twimg.com/media/DOUFsExV4AE2WyL.jpg:large", "author_name": "Xfl",
             "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "circle_id": 122, "circle_name": "columbia buy sell memes"}]


def get_trend_l(trend_id):
    content1 = "The Golden State Warriors are making life difficult for more than " \
               "just their NBA contemporaries.\n\nHoops prognosticators of the bold " \
               "variety, for instance, are having a tricky time dreaming bigger than " \
               "the Dubs' reality.\n\nThey're dominating at once-in-a-generation levels." \
               " They're evolving the sport and challenging long-held beliefs about what's " \
               "possible inside the lines. They might have compiled the best roster ever" \
               " assembled, and each iteration in this run always seems better than the " \
               "last.\n\nThat's why predicting another title for this franchise isn't bold " \
               "enough. While it's not guaranteed, it's the most likely ending to the upcoming " \
               "campaign.\n\nWe're going a little more daring as we delve into five bold " \
               "Warriors' forecasts for 2017-18.\n"
    return {"trend": {"author_id": "1", "like": 0, "trend_id": 123, "like_count": 123, "author_name": "Reggie",
                      "content": content1, "circle_id": 12, "circle_name": "NBA",
                      "image": "https://pbs.twimg.com/media/DOZxjmvV4AEVBge.jpg:large",
                      "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            "comments": [{"author_name": "ReggieYang", "content": "Hello", "author_id": 3,
                          "time": datetime.datetime.now().strftime("%Y-%m-%d")},
                         {"author_name": "Naruhodou", "content": "Hi", "author_id": 123,
                          "time": datetime.datetime.now().strftime("%Y-%m-%d")},
                         {"author_name": "Naruto", "content": "Haha", "author_id": 769,
                          "time": "2017-06-05"}]}


def like_trend_l(moment_id, user_id):
    # print(str(user_id) + 'like' + str(moment_id))
    return 62


def unlike_trend_l(moment_id, user_id):
    # print(str(user_id) + 'unlike' + str(moment_id))
    return 37


def comment_trend_l(comment):
    print(str(comment))
    return


def get_all_circle_l(school_id):
    return [{"circle_id": 12, "circle_name": "Camping is our life",
             "icon": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-0/c68.0.160.160/"
                     "p160x160/15349565_10208953025636274_6871502128788396568_n.jpg?o"
                     "h=a76b7e9557d6becbcf79f447600076c8&oe=5AA1F873",
             "introduction": "This group is like wolf of wall street. there’s buying "
                             "and selling, cutthroat competition and drugs. it’s a stock exchange",
             "announcement": "Buy and cell"},
            {"circle_id": 23, "circle_name": "Photography Beginners", "icon": "", "introduction": "",
             "announcement": ""}]


def join_circle_l(circle_id, user_id):
    print(str(user_id) + "join circle" + str(circle_id))
    return
