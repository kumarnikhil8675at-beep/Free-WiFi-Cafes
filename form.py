from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class cafe_form(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    map_url=StringField("Map_url",validators=[DataRequired()])
    img_url=StringField("Img_url",validators=[DataRequired()])
    location=StringField("Location",validators=[DataRequired()])
    has_sockets=BooleanField("Has_scokets")
    has_toilet=BooleanField("Has_Toilet")
    has_wifi=BooleanField("Has_wifi")
    can_take_calls=BooleanField("Can_take_calls")
    seats=StringField("Seats",validators=[DataRequired()])
    coffee_price=StringField("Coffee_Price",validators=[DataRequired()])
    submit=SubmitField("submit")
    
class login(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    password=StringField("Password", validators=[DataRequired()])
    login=SubmitField("Login")
    

class Sign(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    password=StringField("Password", validators=[DataRequired()])
    register=SubmitField("Register")