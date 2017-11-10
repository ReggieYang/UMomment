import datetime


class Student:
    user_id = -1
    nick_name = ''
    avatar = ''
    school_id = -1
    since = datetime.datetime.now()
    email = ''
    password = ''
    introduction = ''

    # def __init__(self, user_id, nick_name, avatar, school, since, email,
    #              password, introduction):
    #     self.user_id = user_id
    #     self.nick_name = nick_name
    #     self.avatar = avatar
    #     self.school = school
    #     self.since = since
    #     self.email = email
    #     self.password = password
    #     self.introduction = introduction


class Circle:
    circle_id = -1
    circle_name = ''
    icon = ''
    introduction = ''
    school = None
    admin = None
    announcement = ''

    # def __init__(self, circle_id, circle_name, icon, introduction, school,
    #              admin, announcement):
    #     self.circle_id = circle_id
    #     self.circle_name = circle_name
    #     self.icon = icon
    #     self.introduction = introduction
    #     self.school = school
    #     self.admin = admin
    #     self.announcement = announcement


class Followership:
    follower_id = -1
    followed_id = -1
    since = datetime.datetime.now()


class LikingMoment:
    user_id = -1
    moment_id = -1
    time = datetime.datetime.now()


class LikingTrend:
    user_id = -1
    trend_id = -1
    time = datetime.datetime.now()


class Membership:
    member_id = -1
    circle_id = -1
    since = datetime.datetime.now()


class Moment:
    moment_id = -1
    author_id = -1
    content = ''
    image = ''
    time = datetime.datetime.now()


class MomentComment:
    comment_id = -1
    author_id = -1
    to_user = -1
    moment_id = -1
    content = ''
    time = datetime.datetime.now()


class Trend:
    trend_id = -1
    author_id = -1
    circle_id = -1
    content = ''
    image = ''
    time = datetime.datetime.now()


class TrendComment:
    comment_id = -1
    author_id = -1
    trend_id = -1
    content = ''
    time = datetime.datetime.now()
