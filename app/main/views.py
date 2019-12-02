from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
import datetime

from . import main
from .. import db
from ..email import mail_message
from ..requests import get_quotes
from ..models import User,Blogs,Comments,Subscriber
from .forms import BlogForm,CommentForm

# Views
@main.route('/')
def index():
	quotes = get_quotes()
	blogs = Blogs.get_blogs()
	title = 'Blog Post App'
	return render_template('index.html',title = title,blogs = blogs,quotes = quotes)


@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_blog():
	blog_form = BlogForm()
	if blog_form.validate_on_submit():
	    title = blog_form.title.data
	    blog = blog_form.text.data

	    # updating blog instance
	    new_blogs = Blogs(title = title,blog = blog,user = current_user)

	    # save blog
	    new_blogs.save_blogs()
	    return redirect(url_for('.index'))

	title = 'New Blog'
	return render_template('new_blog.html',title = title,blog_form = blog_form)


@main.route('/blog/<int:id>',methods = ['GET','POST'])
def blog(id):
	blog = Blogs.get_single_blog(id)
	published_date = blog.published.strftime('%b %d, %Y')

	comment_form = CommentForm()
	if comment_form.validate_on_submit():
		comment = comment_form.content.data

		new_comment = Comments(comment = comment,user_id = current_user,blog_id = blog)

		new_comment.save_comment()

	comments = Comments.get_comments(blog.id)
    # return render_template('pitch.html', pitch=pitch, comment_form=comment_form, comments=comments, date=posted_date)
	return render_template('blog.html', blog = blog,date = published_date,comment_form = comment_form, comments = comments)


@main.route('/user/<uname>/blogs')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blogs.query.filter_by(user_id = user.id).all()

    return render_template("profile/blogs.html", user=user,blogs=blogs)

@main.route('/subscribe',methods = ['GET','POST'])
def subscribe():
	email = request.form.get('subscriber')
	new_subscriber = Subscriber(email = email)
	new_subscriber.save_subscriber()
	mail_message("Subscribed to Blog Post.","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
	flash('Sucessfuly subscribed')
	return redirect(url_for('main.index'))
