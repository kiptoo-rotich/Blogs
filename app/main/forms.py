from wtforms import StringField,TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class OrderForm(FlaskForm):
    pizza_size=SelectField('Size',validators=[Required()],choices=[('Select your size','Select your size'),(1000,'Large'),(800,'Medium'),(500,'Small')])
    pizza_toppings=SelectField('Toppings',validators=[Required()],choices=[(500,'Broccolini'),(400,'Capers'),(300,'Gorgonzola')])
    pizza_quantity = IntegerField('Quantity',validators=[Required()])
    submit = SubmitField('Submit')