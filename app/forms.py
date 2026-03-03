from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Name is required"),
            Length(min=2, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Enter a valid email address")
        ]
    )

    subject = StringField(
        "Subject",
        validators=[
            DataRequired(message="Subject is required"),
            Length(max=150)
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Message cannot be empty"),
            Length(min=10)
        ]
    )

    submit = SubmitField("Send Message")