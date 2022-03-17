from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    email = StringField('El. paštas', [
        Email(message='Neteisingas adresas.'),
        DataRequired(message='Reikalingas laukas')
    ])

    password = PasswordField('Slaptažodis', [
        Length(min=6, message='slaptažodis per trumpas'),
        DataRequired(message='Reikalingas laukas')
    ])

    address = StringField('Adresas', [DataRequired(message='Reikalingas laukas')])

    address_2 = StringField('Adresas 2')

    city = StringField('Miestas', [DataRequired(message='Reikalingas laukas')])

    state = SelectField(
        'Apskritis',
        choices=["Pasirinkite apskritį", "Vilnius", "Kaunas", "Klaipėda"],
        default="Pasirinkite apskritį"
    )

    zip = StringField('Zip kodas', [
        Length(min=5, message='Įvedėte per mažai skaitmetų zip kodui'),
        DataRequired(message='Reikalingas laukas')
    ])

    check = BooleanField(
        'Pažymėkite, kad sutinkate dalyvauti Squid Games',
        [DataRequired(message='Reikalingas laukas')]
    )

    submit = SubmitField('Užregistruoti')