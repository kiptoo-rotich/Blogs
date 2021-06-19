from flask import render_template,request
from flask_login import current_user, login_required

from .. import db
from .. models import Quotes
from ..requests import get_quote
from . import main
from .forms import BlogForm

#views

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title='Welcome to My Quotes'
    quote = get_quote()
    return render_template('index.html',quote=quote)


@main.route('/home')
@login_required
def main():
    blog_form=BlogForm()
    return render_template('main/main.html',blog_form=blog_form)

