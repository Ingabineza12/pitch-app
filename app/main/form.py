from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Business','Business'),('Product','Product')],validators=[Required()])
    post = TextAreaField('Present your pitch',validators=[Required()])
    submit = SubmitField('Pitch it')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
