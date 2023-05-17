from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("login.html")

@app.route("/re", methods=("GET", "POST"))
def register():
    return render_template("register.html")
app.run()

@app.route('/',methods=['GET','POST'])
def register():
    # request:请求对象 -->获取请求方式、数据
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]):
            # print('数据不完整')
            flash('数据不完整')

        elif password != password2:
            # print('密码不一致')
            flash('密码不一致')
        else:
            # print('完成')
            return 'success'
    return render_template('index.html')
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()