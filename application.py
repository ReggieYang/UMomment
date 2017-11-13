import os
import datetime
from flask import Flask, request, render_template, session, redirect
from flask_cors import CORS
from logic import login, update_student_l, follow, unfollow, get_my_moment, like_moment_l, unlike_moment_l, \
    comment_moment_l, get_comment_momment_l, get_my_trend_l, get_trend_l, unlike_trend_l, like_trend_l, comment_trend_l, \
    get_all_circle_l, join_circle_l, get_schools_l, create_student_l, create_moment_l, get_my_circle, create_trend_l, \
    create_circle_l, my_following, my_follower, get_student_by_name

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
application = Flask(__name__, template_folder=tmpl_dir)
CORS(application)

application.secret_key = 'super secret key'
application.config['SESSION_TYPE'] = 'filesystem'


def args2dict(request_args, args):
    res = {}
    for arg in args:
        res[arg] = request_args.form[arg]
    return res


@application.route('/')
def home_page():
    return render_template('login.html')


@application.route('/register/')
def register_page():
    return render_template('register.html', schools=get_schools_l())


@application.route('/student/create/', methods=['POST'])
def create_student():
    args = ["nick_name", "avatar", "email", "password",
            "introduction", "school_id"]
    student = args2dict(request, args)
    new_student = create_student_l(student)
    session['user'] = new_student
    return redirect('/student/')


@application.route('/student/')
def user_home_page():
    if session['user'] is not None:
        return render_template('user.html')

    else:
        return render_template('error.html')


@application.route('/student/login/', methods=['POST'])
def login_student():
    student_id = request.form['student_id']
    password = request.form['password']
    student = login(student_id, password)
    if student is not None:
        session['user'] = student
        return redirect('/student/')

    else:
        return render_template('error.html')


@application.route('/student/update/', methods=['POST'])
def update_st():
    args = ['user_id', "nick_name", "avatar", "school_id", "since", "email", "password",
            "introduction"]
    student = args2dict(request, args)
    update_student_l(student)
    user_id = request.form['user_id']
    password = request.form['password']
    student = login(user_id, password)
    session['user'] = student
    return redirect('/student/')


@application.route('/student/follow/', methods=['GET', 'POST'])
def set_followship():
    follower = session['user']['user_id']
    if request.method == 'GET':
        following = request.args.get('follower_id')
        if request.args.get('unfollow') == '1':
            unfollow(follower, following)
        else:
            follow(follower, following)
        return redirect('/discover/')
    else:
        following_name = request.form['follower_name']
        following = get_student_by_name(following_name)
        follow(follower, following['user_id'])
        return redirect('/discover/')


@application.route('/discover/', methods=['GET'])
def discover_page():
    user_id = session['user']['user_id']
    following = my_following(user_id)
    follower = my_follower(user_id)
    context = dict(following=following, follower=follower)
    return render_template('discover.html', **context)


@application.route('/circle/create/', methods=['POST'])
def create_circle():
    args = ["introduction", "circle_name", "announcement", 'icon']
    circle = args2dict(request, args)
    circle['admin_id'] = session['user']['user_id']
    circle['time'] = datetime.datetime.now()
    circle['school_id'] = session['user']['school_id']
    create_circle_l(circle)
    return redirect('/circle/')


@application.route('/circle/', methods=['GET'])
def get_circle_school():
    school_id = session['user']['school_id']
    circles = get_all_circle_l(school_id)
    context = dict(circles=circles)
    return render_template('circle.html', **context)


@application.route('/circle/join/', methods=['POST'])
def join_circle():
    circle_id = request.args.get('circle_id')
    user_id = session['user']['user_id']
    join_circle_l(circle_id, user_id)
    return 'success'


@application.route('/trend/', methods=['GET'])
def my_trend():
    user_id = session['user']['user_id']
    trends = get_my_trend_l(user_id)
    my_circles = get_my_circle(user_id)
    context = dict(trends=trends, circles=my_circles)
    return render_template('trend.html', **context)


@application.route('/trend/create/', methods=['POST'])
def post_trend():
    args = ["content", "circle_id", "image"]
    trend = args2dict(request, args)
    trend['author_id'] = session['user']['user_id']
    trend['time'] = datetime.datetime.now()
    create_trend_l(trend)
    return redirect('/trend/')


@application.route('/trend/like/', methods=['POST'])
def like_trend():
    trend_id = request.form['trend_id']
    user_id = session['user']['user_id']
    if request.form['like'] == 'like':
        return str(like_trend_l(trend_id, user_id))
    else:
        return str(unlike_trend_l(trend_id, user_id))


@application.route('/trend/comment/', methods=['POST'])
def comment_trend():
    args = ["content", "trend_id"]
    comment = args2dict(request, args)
    comment['author_id'] = session['user']['user_id']
    comment['time'] = datetime.datetime.now()
    comment_trend_l(comment)
    return 'success'


@application.route('/trendDetail/', methods=['GET'])
def get_trend():
    trend_id = request.args.get('trend_id')
    trend = get_trend_l(trend_id)
    context = dict(trend=trend)
    return render_template('trend_detail.html', **context)


@application.route('/moment/create/', methods=['POST'])
def post_moment():
    args = ["content", "image"]
    moment = args2dict(request, args)
    moment['author_id'] = session['user']['user_id']
    moment['time'] = datetime.datetime.now()
    create_moment_l(moment)
    return redirect('/moment/')


@application.route('/moment/like/', methods=['POST'])
def like_moment():
    moment_id = request.form['moment_id']
    user_id = session['user']['user_id']
    if request.form['like'] == 'like':
        return str(like_moment_l(moment_id, user_id))
    else:
        return str(unlike_moment_l(moment_id, user_id))


@application.route('/moment/comment/', methods=['POST'])
def comment_moment():
    args = ["content", "moment_id", "to_user"]
    comment = args2dict(request, args)
    comment['author_id'] = session['user']['user_id']
    comment['time'] = datetime.datetime.now()
    comment_moment_l(comment)
    return 'success'


@application.route('/moment/', methods=['GET'])
def get_all_moment():
    user_id = session['user']['user_id']
    moments = get_my_moment(user_id)
    context = dict(moments=moments)
    return render_template('moment.html', **context)


@application.route('/moment/findComment/', methods=['POST'])
def get_moment_comment():
    comments = get_comment_momment_l(request.form['moment_id'])
    session['comments'] = comments
    return 'success'


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=6565, debug=True)
