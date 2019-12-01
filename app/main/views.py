from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
import datetime

from . import main
from .. import db
from ..models import User,Blogs
from .forms import BlogForm

# Views
@main.route('/')
def index():
	blogs = Blogs.get_blogs()
	title = 'Blog Post App'
	return render_template('index.html',title = title,blogs = blogs)


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

    # comment_form = CommentForm()
    # if comment_form.validate_on_submit():
    #     comment = comment_form.text.data
	#
    #     new_comment = Comment(comment = comment,user_id = current_user,pitch_id = pitch)
	#
    #     new_comment.save_comment()
	#
    # comments = Comment.get_comments(pitch.id)
    # return render_template('pitch.html', pitch=pitch, comment_form=comment_form, comments=comments, date=posted_date)
    return render_template('blog.html', blog = blog,date = published_date)
