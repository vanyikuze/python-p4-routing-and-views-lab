#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    # Print the string to the console
    print(string)
    # Display the string in the web browser
    return string

@app.route('/count/<int:num>')
def count(num):
    # Create a string with numbers in the specified range
    numbers = '\n'.join(str(i) for i in range(num))
    # Display the numbers in the web browser
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Division by zero is not allowed.'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation.'

if __name__ == '__main__':
    app.run(debug=True)

