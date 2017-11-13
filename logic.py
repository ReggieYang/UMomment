import json

import datetime

from dao.student_dao import find_student, update_student, follow, unfollow, find_student_by_nickname, \
    find_my_followings, find_my_followers, find_all_schools, create_student, insert_moment, unlike_moment, like_moment, \
    comment_trend, comment_moment, post_trend, like_trend, unlike_trend, post_circle, join_circle, find_circles_join, \
    find_moments


def login(student_id, password):
    student = find_student(student_id)
    if student['password'] == password:
        return student
    else:
        return None


def get_schools_l():
    return find_all_schools()


def get_student_l(user_id):
    return find_student(user_id)


def create_student_l(student):
    student['since'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    create_student(student)
    return find_student(get_student_by_name(student['nick_name'])['user_id'])


def get_student_by_name(nick_name):
    return find_student_by_nickname(nick_name)


def update_student_l(student):
    user_id = student['user_id']
    student.pop('user_id', None)
    update_student(user_id, student)


def follow_l(user_id, following_id):
    follow(user_id, following_id, datetime.datetime.now())
    return


def unfollow_l(user_id, following_id):
    unfollow(user_id, following_id)
    return


def my_following(user_id):
    return find_my_followings(user_id)


def my_follower(user_id):
    return find_my_followers(user_id)


def get_my_moment(user_id):
    moments = find_moments(user_id)
    for i in range(0, len(moments)):
        moments[i]['time'] = moments[i]['time'].strftime("%Y-%m-%d %H:%M")
    return moments


def like_moment_l(moment_id, user_id):
    like_moment({"moment_id": moment_id, "user_id": user_id, "time": str(datetime.datetime.now())})
    return


def unlike_moment_l(moment_id, user_id):
    unlike_moment(user_id, moment_id)
    return


def comment_moment_l(comment):
    comment['time'] = str(datetime.datetime.now())
    comment['to_user'] = get_student_by_name(comment['to_user'])['user_id']
    comment_moment(comment)
    return


def create_moment_l(moment):
    moment['time'] = str(datetime.datetime.now())
    insert_moment(moment)
    return


def get_comment_momment_l(moment_id):
    return [{"nick_name": "ReggieYang", "to_user": "Xfl", "content": "Hello", "author_id": 3,
             "time": datetime.datetime.now().strftime("%Y-%m-%d")},
            {"nick_name": "Naruhodou", "to_user": "Mitsurugi", "content": "Hi", "author_id": 123,
             "time": datetime.datetime.now().strftime("%Y-%m-%d")},
            {"nick_name": "Naruto", "to_user": "Sasuke", "content": "Haha", "author_id": 769,
             "time": "2017-06-05"}]


def get_my_trend_l(user_id):
    content1 = "Philadelphia center Joel Embiid has agreed to a five-year, $148 million " \
               "designated rookie scale max extension, league sources told ESPN."
    content2 = "The Golden State Warriors are making life difficult for more than just " \
               "their NBA contemporaries."
    # need a select on several tables, similar to what we wrote in the first part --- one of those 3 sql
    return [{"author_id": "1", "trend_id": 123, "like_count": 123, "author_name": "Reggie",
             "content": content1[0:50], "circle_id": 12, "circle_name": "NBA",
             "image": "", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"author_id": "2", "content": content2[0:50], "trend_id": 12, "like_count": 3,
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
    return {"trend": {"author_id": "1", "like": 0, "trend_id": 1, "like_count": 123, "nick_name": "Reggie",
                      "content": content1, "circle_id": 12, "circle_name": "NBA",
                      "image": "https://pbs.twimg.com/media/DOZxjmvV4AEVBge.jpg:large",
                      "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            "comments": [{"nick_name": "ReggieYang", "content": "Hello", "author_id": 3,
                          "time": datetime.datetime.now().strftime("%Y-%m-%d")},
                         {"nick_name": "Naruhodou", "content": "Hi", "author_id": 123,
                          "time": datetime.datetime.now().strftime("%Y-%m-%d")},
                         {"nick_name": "Naruto", "content": "Haha", "author_id": 769,
                          "time": "2017-06-05"}]}


def like_trend_l(trend_id, user_id):
    like_trend({"trend_id": trend_id, "user_id": user_id, "time": str(datetime.datetime.now())})
    return


def unlike_trend_l(trend_id, user_id):
    unlike_trend(user_id, trend_id)
    return


def create_trend_l(trend):
    trend['time'] = str(datetime.datetime.now())
    post_trend(trend)
    return


def comment_trend_l(comment):
    comment['time'] = str(datetime.datetime.now())
    comment_trend(comment)
    return


def get_my_circle(user_id):
    return find_circles_join(user_id)


def create_circle_l(circle):
    post_circle(circle)
    return


def get_all_circle_l(school_id):
    return [{"circle_id": 4, "circle_name": "Camping is our life",
             "icon": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-0/c68.0.160.160/"
                     "p160x160/15349565_10208953025636274_6871502128788396568_n.jpg?o"
                     "h=a76b7e9557d6becbcf79f447600076c8&oe=5AA1F873",
             "introduction": "This group is like wolf of wall street. there’s buying "
                             "and selling, cutthroat competition and drugs. it’s a stock exchange",
             "announcement": "Buy and cell", "admin_id": 12, "admin_name": "Harden"},
            {"circle_id": 5, "circle_name": "Photography Beginners", "icon": "", "introduction": "",
             "announcement": "", "admin_id": 1, "admin_name": "Rudy"}]


def join_circle_l(circle_id, user_id):
    join_circle(user_id, circle_id, str(datetime.datetime.now()))
    return
