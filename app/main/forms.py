from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,ValidationError,TextAreaField
from flask_login import current_user
from wtforms.fields.simple import FileField,FileAllowed
from ..models import User
from wtforms.validators import Required,Email

class ProfileUpdate(FlaskForm):
    username = StringField('Enter username',validators=[Required()])
    email = StringField('Enter email',validators=[Required(),Email()])
    bio = TextAreaField('Brief bio about you',validators=[Required()])
    profile_picture = FileField('profile photo',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The email is already picked!!")

    def validate_username(self,username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username is already taken!!")

class Blog(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Blog content',validators=[Required()])
    submit = SubmitField('Post')