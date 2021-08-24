import os
import secrets

from flask import render_template,url_for,flash, redirect,request,abort
from flask3 import app,db,bcrypt
from flask3.forms import RegistrationForm, LoginForm,UpdateAccountForm,PostForm,CommentsForm
from flask3.models import User,Post,Comment,Quote
from flask_login import login_user,current_user,logout_user,login_required

quotes=[
    {
        "author": "Brian Kernighan",
        "id": 5,
        "quote": "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.",
        "permalink": "http://quotes.stormconsultancy.co.uk/quotes/5"
    }
 ]

@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
   
    return render_template('home.html',posts= posts)
@app.route('/about')
def about():
    return render_template('about.html',title= "about")

@app.route('/register',methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
       return redirect(url_for('home'))
   form =RegistrationForm()
   if form.validate_on_submit():
       hashed_password =bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user= User(username=form.username.data, email=form.email.data, password=hashed_password)
       db.session.add(user)
       db.session.commit()
       flash('Your account has been created! You are now able to log in', 'success')
       return redirect(url_for('login'))

   return render_template('register.html',title="register", form= form)