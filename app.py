from flask import Flask, render_template, url_for
from form import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '605c89ab0256f331e0a1b2ec2f08c646'


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/home/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
