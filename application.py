import json

import os
from flask import Flask, request, render_template, session, redirect
from flask_cors import CORS

from logic import login, update_student_l, follow, unfollow, get_my_moment, like_moment_l, unlike_moment_l

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


@application.route('/student/follow/', methods=['POST'])
def set_followship():
    follower = request.form['follower_id']
    following = request.form['following_id']
    if request.form['unfollow'] == 1:
        unfollow(follower, following)
    else:
        follow(follower, following)


@application.route('/school/show/', methods=['POST'])
def get_school():
    return


@application.route('/school/showStudent/', methods=['POST'])
def get_student():
    return


@application.route('/group/create/', methods=['POST'])
def create_group():
    return


@application.route('/group/join/', methods=['POST'])
def join_group():
    return


@application.route('/group/leave/', methods=['POST'])
def leave_group():
    return


@application.route('/trend/delete/', methods=['POST'])
def delete_trend():
    return


@application.route('/trend/create/', methods=['POST'])
def post_trend():
    return


@application.route('/trend/like/', methods=['POST'])
def like_trend():
    return


@application.route('/trend/comment/', methods=['POST'])
def comment_trend():
    return


@application.route('/trend/find/', methods=['POST'])
def get_trend():
    return


@application.route('/moment/delete/', methods=['POST'])
def delete_moment():
    return


@application.route('/moment/create/', methods=['POST'])
def post_moment():
    return


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
    return


@application.route('/moment/', methods=['GET'])
def get_all_moment():
    user_id = session['user']['user_id']
    moments = get_my_moment(user_id)
    session['my_moments'] = moments
    return render_template('moment.html')


@application.route('/moment/find/', methods=['POST'])
def get_moment():
    # return render_template('moment.html')
    return


# @application.route('/search/<keyword>')
# def show_post(keyword):
#     es = es_conn()
#     resp = flask.Response(parse_res(es, keyword))
#     resp.headers['Content-Type'] = 'application/json'
#     return resp


if __name__ == '__main__':
    # application.secret_key = 'super secret key'
    # application.config['SESSION_TYPE'] = 'filesystem'

    # application.debug = True

    application.run(host='127.0.0.1', port=6565, debug=True)
