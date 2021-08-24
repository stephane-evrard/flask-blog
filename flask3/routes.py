import os
import secrets

from flask import render_template,url_for,flash, redirect,request,abort
from flask3 import app,db,bcrypt
from flask3.forms import RegistrationForm, LoginForm,UpdateAccountForm,PostForm,CommentsForm
from flask3.models import User,Post,Comment,Quote
from flask_login import login_user,current_user,logout_user,login_required
