import json
from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from functools import wraps
from bot import query_gpt

from db import add_chat_record, add_user, check_credentials, get_user_chat_records

app = Flask(__name__)
app.secret_key = 'chatbot20230519'


def must_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        
        return func(*args, **kwargs)
    
    return decorated_function


@app.route("/", methods=("GET", "POST"))
@must_login
def index():
    # redirect to chat page
    return redirect(url_for('robot'))


@app.route("/robot", methods=("GET", "POST"))
@must_login
def robot():
    if request.method == 'POST':
        response = {'code': 200}
        question = request.args.get("spoken")
        # get answer from gpt
        print(f"question {question}")
        answer = query_gpt(question)
        if answer is None:
            answer = 'something wrong, try again'
            
        response['answer'] = answer

        # save question and answer to db
        add_chat_record(question, answer, session.get("username"))

        return jsonify(response)
    
    chat_records = get_user_chat_records(session.get("username"))
    return render_template("robot.html", chat_records=chat_records)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get request arguments
        post_data = request.get_json()
        username = post_data.get('username', None)
        password = post_data.get('password', None)

        response = {'code': 200}
        if not all([username, password]):
            response['code'] = 400
            response['msg'] = 'illegal username or password'
            return jsonify(response)
        else:
            # check user password
            user = check_credentials(username, password)
            if not user:
                response['code'] = 400
                response['msg'] = "invalid password"
            else:
                # add user to session
                session['username'] = username

            return jsonify(response)

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # request:请求对象 -->获取请求方式、数据
    if request.method == 'POST':
        # 获取请求参数
        post_data = request.get_json()
        username = post_data.get('username', None)
        password = post_data.get('password', None)
        print(f"get {username} {password}")

        response = {'code': 200}
        if not all([username, password]):
            response['code'] = 400
            response['msg'] = 'illegal username or password'
            return jsonify(response)
        else:
            # add user to database
            success, msg = add_user(username, password)
            if not success:
                response['code'] = 400
                response['msg'] = msg

            return jsonify(response)
        
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
