from flask_login import login_user,login_required,logout_user
from flask import render_template,flash,url_for,redirect,request
from app.auth import auth
from .forms import RegistrationForm,LoginForm
from ..email import mail_message
from app.models import User

@auth.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Credentials(check password/username)')
    return render_template('auth/login.html',form = form)

@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.usernam.data,email = form.email.data,password = form.password.data)
        user.save()
        mail_message("Welcome to Blog-Web","email/welcome",user.email,user = user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',regform = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
    