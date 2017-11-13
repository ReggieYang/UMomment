import json
from sqlalchemy import *
import datetime

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  # No logging
metadata = MetaData(db)

student = Table('student', metadata, autoload=True)
followership = Table('followership', metadata, autoload=True)
membership = Table('membership', metadata, autoload=True)
circle = Table('circle', metadata, autoload=True)
moment = Table('moment', metadata, autoload=True)
likingmoment = Table('likingmoment', metadata, autoload=True)
momentcomment = Table('momentcomment', metadata, autoload=True)
trend = Table('trend', metadata, autoload=True)
likingtrend = Table('likingtrend', metadata, autoload=True)
trendcomment = Table('trendcomment', metadata, autoload=True)
school = Table('school', metadata, autoload=True)


def quotevalue(value):
    statement = ''
    if type(value) == type('a'):
        statement += "'"
    statement += str(value)
    if type(value) == type('a'):
        statement += "'"
    return statement


def row2dict(row):
    d = {}
    for rs in row.keys():
        d[rs] = row[rs]
    return d


def multirow2listdict(row):
    list = []
    for rs in row:
        dict = {}
        for key in rs.keys():
            dict[key] = rs[key]
        list.append(dict)
    return list


def create_student(info):
    statement = "INSERT INTO student ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    # i = student.insert()
    # i.execute(user_id=s['user_id'], nick_name=s['nick_name'], avatar=s['avatar'], school_id=s['school_id'],
    #           since=s['since'], email=s['email'], password=s['password'],
    #           introduction=s['introduction'])
    return


def find_student(id):
    result = student.select(student.c.user_id == id)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    # s = {'user_id': rs.user_id, 'nick_name': rs.nick_name, 'avatar': rs.avatar, 'school_id': rs.school_id,
    #      'since': rs.since, 'email': rs.email, 'password': rs.password, 'introduction': rs.introduction}
    s = row2dict(rs)
    return s


# All the info about update
def update_student(id, info):
    statement = "UPDATE student SET "
    for key in info:
        statement += key
        statement += '='
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ' WHERE user_id='
    statement += str(id)
    db.execute(statement)
    return


def follow(followerid, followedid, sincetime):
    i = followership.insert()
    i.execute(follower_id=followerid, followed_id=followedid, since=sincetime)
    return


def unfollow(followerid, followedid):
    statement = "DELETE FROM followership WHERE follower_id="
    statement += str(followerid)
    statement += " and followed_id="
    statement += str(followedid)
    db.execute(statement)
    return


def find_student_by_nickname(nickname):
    result = student.select(student.c.nick_name == nickname)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    s = {}
    s['user_id'] = rs.user_id
    return s


# find those users that I follow
def find_my_followings(userid):
    followingid = followership.select(followership.c.follower_id == userid).alias("follwingid")
    result = student.select(student.c.user_id == followingid.c.followed_id)
    rs = result.execute()
    d = multirow2listdict(rs)
    return d


# find those users that follow me
def find_my_followers(userid):
    followedid = followership.select(followership.c.followed_id == userid).alias("followedid")
    result = student.select(student.c.user_id == followedid.c.follower_id)
    rs = result.execute()
    d = multirow2listdict(rs)
    return d


# info = {'circle_id':10, 'circle_name':'yes', 'introduction':'Test for post circle', 'school_id':5, 'admin_id':4}
def post_circle(info):
    statement = "INSERT INTO circle ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def join_circle(userid, circleid, sincetime):
    i = membership.insert()
    i.execute(member_id=userid, circle_id=circleid, since=sincetime)
    return


def find_circle(circleid):
    result = circle.select(circle.c.circle_id == circleid)
    resultExe = result.execute()
    rs = resultExe.fetchone()
    s = row2dict(rs)
    return s


def find_circles_join(userid):
    circleid = membership.select(membership.c.member_id == userid).alias("circleid")
    result = circle.select(circle.c.circle_id == circleid.c.circle_id)
    rs = result.execute()
    d = multirow2listdict(rs)
    return d


# return all the pairs of school id and school name
def find_all_schools():
    s = school.select()
    rs = s.execute()
    d = multirow2listdict(rs)
    return d


# find the moments of mine and the people I follow
def find_moments(userid):
    statement = "SELECT moment.*, s1.nick_name, like_new_moment.like_or_not, like_new_moment.liking_count FROM moment, (SELECT new_moment.moment_id, CASE @ IN (SELECT lm.user_id FROM likingmoment lm WHERE lm.moment_id = new_moment.moment_id) WHEN TRUE THEN 1 ELSE 0 END AS like_or_not, count(likingmoment.user_id) AS liking_count FROM (SELECT moment.* FROM moment, (SELECT DISTINCT followed_id AS user_id FROM followership WHERE followed_id = @ OR follower_id = @) AS friend WHERE moment.author_id = friend.user_id ORDER BY moment.time LIMIT 20) AS new_moment LEFT JOIN likingmoment ON new_moment.moment_id = likingmoment.moment_id GROUP BY new_moment.moment_id) AS like_new_moment, student s1 WHERE moment.moment_id = like_new_moment.moment_id AND moment.author_id = s1.user_id ORDER BY liking_count DESC"
    statement = statement.replace("@", str(userid))
    result = db.execute(statement)
    d = multirow2listdict(result)
    return d


# info = {'moment_id':55, 'author_id': 5, 'content': 'yeah', 'time':'2017-10-09 19:28:30.824310'}
def insert_moment(info):
    statement = "INSERT INTO moment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


# info = {'user_id':9, 'moment_id':41, 'time':'2017-10-09 19:42:43.579866'}
def like_moment(info):
    statement = "INSERT INTO likingmoment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def unlike_moment(userid, momentid):
    statement = "DELETE FROM likingmoment WHERE user_id="
    statement += str(userid)
    statement += " and moment_id="
    statement += str(momentid)
    db.execute(statement)
    return


# info = {'comment_id':12,'author_id':9,'to_user':1,'moment_id':55,'content':'yyyy','time':'2017-10-09 21:38:44.677678'}
def comment_moment(info):
    statement = "INSERT INTO momentcomment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return

def find_trends_in_circles(userid):
    circleid = membership.select(membership.c.member_id == userid).alias("circleid")
    trends = trend.select(circleid.c.circle_id==trend.c.circle_id)
    result = trends.execute()
    d = multirow2listdict(result)
    return d

# def find_comments_of_momment(momentid):
#     commentinfo = momentcomment.select(momentcomment.c.moment_id==momentid).alias("commentinfo")
#     commentinfoall = select([student.c.user_id,])

def find_trend_comments(trendid):
    trendinfo = trend.select(trendid==trend.c.trend_id)
    result = {}
    trendexe = trendinfo.execute()
    trendone = trendexe.fetchone()
    result["trend"] = row2dict(trendone)
    trendinfo2 = trend.select(trendid == trend.c.trend_id).alias("trendinfo2")
    commentinfo = trendcomment.select(trendcomment.c.trend_id==trendinfo2.c.trend_id).alias("commentinfo")
    commentinfofull = select([student.c.nick_name, commentinfo],student.c.user_id==commentinfo.c.author_id)
    commentexe = commentinfofull.execute()
    result["comment"] = multirow2listdict(commentexe)
    return result




# info = {'trend_id':11, 'author_id':4, 'circle_id':2, 'content':'yyyy', 'time':'2017-10-09 21:47:31.127708'}
def post_trend(info):
    statement = "INSERT INTO trend ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def like_trend(info):
    statement = "INSERT INTO likingtrend ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return


def unlike_trend(userid, trendid):
    statement = "DELETE FROM likingtrend WHERE user_id="
    statement += str(userid)
    statement += " and trend_id="
    statement += str(trendid)
    db.execute(statement)
    return


# info = {'comment_id': 13, 'author_id': 6, 'trend_id': 11, 'content': 'nnnn', 'time': '2017-10-09 21:47:31.127708'}
def comment_trend(info):
    statement = "INSERT INTO trendcomment ("
    for key in info:
        statement += key
        statement += ','
    statement = statement[0:-1]
    statement += ') VALUES ('
    for key in info:
        statement += quotevalue(info[key])
        statement += ','
    statement = statement[0:-1]
    statement += ')'
    db.execute(statement)
    return
