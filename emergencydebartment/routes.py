from flask import  render_template, url_for ,flash,redirect
from emergencydebartment import app
from emergencydebartment.form import LoginForm
from emergencydebartment.models import Admin






@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('adminhome.html')


@app.route("/home/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form)
    if form.validate_on_submit():
        
        if form.username.data == 'admin' and form.password.data == 'admin':
            
            flash('you have been log in, admin', 'success')
            return redirect(url_for('admin'))
    else:
        flash('login unsuccessful please check username and password','danger')
    return render_template("login.html", form=form )
