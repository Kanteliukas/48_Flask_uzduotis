from flask import Flask, request, render_template
from dictionary import data
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bet kokia simbolių eilutė'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        address_line = request.form["address"]
        adress_line2 = request.form["address_2"]
        city = request.form["city"]
        state = request.form["state"]
        zip = request.form["zip"]
        data.append({
            'email': email,
            'password': password,
            'address': address_line,
            'address_2': adress_line2,
            'city': city,
            'state': state,
            'zip': zip,
        })
        return render_template('success_page.html', data=data, form=[])
    return render_template('form.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('success_page.html', form=form, data=[])
    return render_template('form2.html', form=form)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)