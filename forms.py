from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):

    email = StringField('El. paštas', [Email(message='Neteisingas adresas.'), DataRequired()])
    password = PasswordField('Slaptažodis', [Length(min=6, message='slaptažodis per trumpas'), DataRequired()])
    address = StringField('Adresas', [DataRequired()])
    address_2 = StringField('Adresas 2')
    city = StringField('Miestas', [DataRequired()])
    state = SelectField('Apskritis', choices=["Pasirinkite apskritį", "Vilnius", "Kaunas", "Klaipėda"], default="Pasirinkite apskritį")
    zip = StringField('Zip kodas', [Length(min=5, message='Įvedėte per mažai skaitmetų zip kodui'), DataRequired()])
    check = BooleanField('Pažymėkite, kad sutinkate dalyvauti Squid Games', [DataRequired()])
    submit = SubmitField('Užregistruoti')