from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    '''
    Class that will define the form to create a pitch
    '''

    pitch = TextAreaField('Enter your pitch', validators=[Required()])
    pitch_category = RadioField('Choose your pitch category', validators=[Required()], choices=[('interview'), ('promotion'), ('comedy'), ('pickup')])
    submit = SubmitField('pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself :)', validators = [Required()])
    submit = SubmitField('submit')