import json

import flask
from flask import Flask, request
from flask_cors import CORS

from logic.student_logic import test_login

application = Flask(__name__)
CORS(application)


@application.route('/')
def hello_world():
    return "Hello, welcome to twittMap API!"


@application.route('/test/', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        res = {"un": username, "pw": password}
        # resp = flask.Response({"un": username, "pw": password})
        # resp.headers['Content-Type'] = 'application/json'
        return test_login(username, password)
    return 'hahaha'


# @application.route('/search/<keyword>')
# def show_post(keyword):
#     es = es_conn()
#     resp = flask.Response(parse_res(es, keyword))
#     resp.headers['Content-Type'] = 'application/json'
#     return resp


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=6565, debug=True)
