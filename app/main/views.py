from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .. import db
from ..models import Blog, Quotes,Comment,User
from ..requests import get_quote
from . import main
from ..email import mail_message
from .forms import BlogForm,CommentForm

#views

@main.route('/',methods=['GET'])
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title='Welcome to My Quotes'
    quote = get_quote()
    return render_template('index.html',quote=quote)


@main.route('/home',methods=['GET','POST'])
@login_required
def main_page():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog_category=blog_form.blog_category.data
        blog_title=blog_form.blog_title.data
        blog_content=blog_form.blog_content.data
        
        new_blog=Blog(blog_category=blog_category,blog_title=blog_title,blog_content=blog_content)
        # email=User.query.filter_by(email).all()
        
        # mail_message("Welcome to PizzaPlace","email/newpost",blog_category=blog_category)

        
        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.main_page'))
    else:
        blogs=Blog.query.order_by(Blog.posted).all()
    return render_template('main_templates/main.html',blog_form=blog_form, blogs=blogs)

@main.route('/comments/<int:id>',methods=['GET','POST'])
@login_required
def comments(id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit:
        comment_data=comment_form.blog_comment.data
        
        new_comment=Comment(comment=comment_data)
        
        new_comment.save_comment()
        db.session.add(new_comment)
        db.session.commit()
        
    comm =Comment.get_comment(id)
        
    return render_template('main_templates/comment.html',comment_form=comment_form,comm=comm)

