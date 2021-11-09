from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
    '''
    Class that will define the form to create a pitch
    '''

    pitch = TextAreaField('Enter your pitch', validators=[InputRequired()])
    pitch_category = RadioField('Choose your pitch category', validators=[InputRequired()], choices=[('Interview'), ('Promotion'), ('Comedy'), ('Pickup Lines')])
    submit = SubmitField('pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself :)', validators = [InputRequired()])
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment...', validators=[InputRequired()])
    submit = SubmitField('comment')