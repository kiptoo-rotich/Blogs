from wtforms import StringField,TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class BlogForm(FlaskForm):
    blog_category=SelectField('Category',validators=[Required()],choices=[('Select your blog category','Select your blog category'),('Technology','Technology'),('Sports','Sports'),('Politics','Politics'),('Adventure','Adventure'),('Agriculture','Agriculture'),('Business',"Business"),('Others',"Others")])
    blog_title=StringField('Title',validators=[Required()])
    blog_content=TextAreaField('Content',validators=[Required()])
    submit = SubmitField('Submit')
    
class Comment(FlaskForm):
    blog_comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('Comment')