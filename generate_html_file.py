import os

BRACKET_LEFT = '{'
BRACKET_RIGHT = '}'
DOUBLE_BRACKET_LEFT = '{{'
DOUBLE_BRACKET_RIGHT = '}}'
CURRENT_DIRECTORY = os.getcwd()

def prepare_check_data(element, ending_element):
    data = f'''{DOUBLE_BRACKET_LEFT} form.{element}(class="form-check-input") {DOUBLE_BRACKET_RIGHT}
        {DOUBLE_BRACKET_LEFT} form.{element}.label(class="form-check-label") {DOUBLE_BRACKET_RIGHT}
        {ending_element}'''

    return data

def prepare_data():
    fields = ["email", "password", "address", "address_2", "city", "state", "zip", "check"]
    add_placeholder = ["address", "address_2", "state"]
    data = {}
    placeholder = {
        "address": "Buto numeris",
        "address_2": "123 Laisvės pr.",
        "state": "Pasirinkite apskritį",
    }
    form_element_left = f'{DOUBLE_BRACKET_LEFT} form.'

    for element in fields:
        form_element_right = f'(class="form-control") {DOUBLE_BRACKET_RIGHT}'
        ending_element = f'''{BRACKET_LEFT}% if form.{element}.errors %{BRACKET_RIGHT}
                    {BRACKET_LEFT}% for error in form.{element}.errors %{BRACKET_RIGHT}
                    <small><font color="red"> {DOUBLE_BRACKET_LEFT}error{DOUBLE_BRACKET_RIGHT} </font></small>
                    {BRACKET_LEFT}% endfor %{BRACKET_RIGHT}
                    {BRACKET_LEFT}% endif %{BRACKET_RIGHT}'''

        if element == "check":
            data[element] = prepare_check_data(element, ending_element)
        else:
            if element in add_placeholder:
                form_element_right = f'(class="form-control", placeholder="{placeholder[element]}") {DOUBLE_BRACKET_RIGHT}'

            data[element] = f'''{DOUBLE_BRACKET_LEFT} form.{element}.label(class="form-control-label") {DOUBLE_BRACKET_RIGHT}
                {form_element_left}{element}{form_element_right}
                {ending_element}'''

    return data

def generate_html():
    data = prepare_data()

    with open(f"{CURRENT_DIRECTORY}\\templates\\html_template.html", "r") as file:
        html = file.read()

    for element in data.keys():
        html = html.replace(f"{element}_placeholder", data[element])

    return html
