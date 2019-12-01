from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
import datetime

from . import main
from .. import db

# Views
@main.route('/')
def index():
	title = 'Blog Post App'
	return render_template('index.html',title = title)
