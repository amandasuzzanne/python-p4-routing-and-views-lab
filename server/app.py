#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

@app.route('/math/<int:number1>/<string:operation>/<int:number2>')
def math(number1, number2, operation):
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)
    elif operation == 'div':
        return str(number1 / number2)
    elif operation == '%':
        return str(number1 % number2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
