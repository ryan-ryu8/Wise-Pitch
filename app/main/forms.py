from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,Boolean,TextAreaField, SelectField, RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

