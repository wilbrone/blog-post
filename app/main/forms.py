from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    """docstring for PitchForm."""

    title = StringField('Blog title', validators = [Required()])
    text = TextAreaField('Content', validators = [Required()])
    submit = SubmitField('Publish')

class CommentForm(FlaskForm):
    """docstring for CommentForm."""

    text = TextAreaField('Leave a Comment:', validators = [Required()])
    submit = SubmitField('Post')
