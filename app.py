from flask import Flask, request, render_template, render_template_string
from forms import RegistrationForm
from generate_html_file import generate_html

app = Flask(__name__)

app.config['SECRET_KEY'] = 'xxxxxx'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = [dict(request.form)]
        return render_template('success_page.html', data=data, form=[])
    return render_template('form.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('success_page.html', form=form, data=[])
    return render_template('form2.html', form=form)

@app.route('/third_option', methods=['GET', 'POST'])
def third_option():
    form = RegistrationForm()
    html = generate_html()
    if form.validate_on_submit():
        return render_template('success_page.html', form=form, data=[])
    #https://www.fullstackpython.com/flask-templating-render-template-string-examples.html
    return render_template_string(html, form=form)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)