from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,ValidationError,PasswordField,BooleanField
from ..models import User
from wtforms.validators import Required,Email,Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Enter username', validators=[Required(),Length(min = 4,max = 20)])
    email = StringField('Your email',validators=[Required(),Email()])
    password = PasswordField('Password to use', validators=[Required(),EqualTo('password_confirm',message = 'Passwords need to match')])
    password_confirm = PasswordField('Confirm entered password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError(message = "Email already picked!!")

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError(message = "Username already picked!!")