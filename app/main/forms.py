from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,Boolean,TextAreaField, SelectField, RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('Post your wise-pitch')
    submit = SubmitField('Submit my pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote = RadioField('default field arguments', choices=[('1', 'Like'), ('1', 'Unlike')])

class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()
