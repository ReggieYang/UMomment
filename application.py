import json

import flask
import os
from flask import Flask, request, render_template
from flask_cors import CORS

from logic.student_logic import login

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
application = Flask(__name__, template_folder=tmpl_dir)
CORS(application)


@application.route('/')
def home_page():
    return render_template('login.html')


@application.route('/student/login/', methods=['POST'])
def student_login():
    if request.method == "POST":
        id = request.form['id']
        password = request.form['password']
        student = login(id, password)
        print(id)
        print(password)
        if student is not None:
            context = dict(data=student)
            return render_template('user.html', **context)

        else:
            # return render_template('error.html')
            return 'error'


# @application.route('/search/<keyword>')
# def show_post(keyword):
#     es = es_conn()
#     resp = flask.Response(parse_res(es, keyword))
#     resp.headers['Content-Type'] = 'application/json'
#     return resp


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=6565, debug=True)
