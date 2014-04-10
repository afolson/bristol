from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField 
from wtforms.validators import ValidationError, Required, Length, \
    Email, Regexp


class SignupForm(Form):

    username = TextField('Username:', [
        Length(max=16, message='Username too long.'),
        Regexp('\w', message='Illegal username.'),
        Required(message='Enter your Minecraft Username.')
    ])

    email = TextField('Email Address:', [
        Length(min=6,
               max=320,
               message='Email too long/short.'),
       Required(message='Enter your email address.'),
       Email(message='Invaid Email address.')
    ])

    recaptcha = RecaptchaField()
