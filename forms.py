from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, validators
from wtforms.validators import InputRequired, Email, ValidationError
#from wtforms_html5 import EmailField, TelField, TextField


def validate_phone(form, field):
    is_digit = field.data.isDigit()
    is_greater_than_nine = (len(field.data) >= 9)
    valid = is_digit and is_greater_than_nine
    if not valid:
        raise ValidationError('Please enter a valid phone number')


class ContactForm(Form):
    name = TextField('Name', [InputRequired()])
    email = TextField('Email', [Email(), InputRequired()])
    phone = TextField('Phone')
    subject = TextField('Subject', [InputRequired()])
    message = TextAreaField('Message', [InputRequired()])
