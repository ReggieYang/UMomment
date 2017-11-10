import json

from vo import Student


def test_login(username, password):
    st = Student()
    st.email = 'ss'
    st.introduction = 'aa'
    return st.introduction
