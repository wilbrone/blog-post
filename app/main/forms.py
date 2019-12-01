from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    """docstring for PitchForm."""

    title = StringField('Blog title', validators = [Required()])
    text = TextAreaField('Content', validators = [Required()])
    submit = SubmitField('Submit')
