from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, FileField
from wtforms.validators import Required, Length, Email, Regexp


class SignupForm(Form):

    username = TextField('Username:', [
        Length(max=16, message='Username too long.'),
        Regexp('\w', message='Illegal username.'),
        Required(message='Enter your Minecraft Username.')
    ])

    name = TextField('Full name:', [
        Length(max=50, message='Name too long.'),
        Required(message='Enter your full name.')
    ])

    email = TextField('Email Address:', [
        Length(min=6,
               max=320,
               message='Email too long/short.'),
        Required(message='Enter your email address.'),
        Email(message='Invaid Email address.')
    ])

    password = PasswordField('Password:', [
        Required(message='Missing password.'),
    ])

    recaptcha = RecaptchaField()


class PoopForm(Form):
    description = TextField('How was your poop?', [
        Length(max=128, message='Your poop description is too long.'),
        Required(message='Tell us how your poop was.'),
    ])

    image = FileField('Upload a picture of yer turd')
