#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:statement>")
def print_string(statement):
    print(statement)  
    return f"{statement}"


@app.route("/count/<int:number>")
def count(number):
    numbers = ''
    for i in range(number):
        numbers += str(i) + '\n'
    return numbers


@app.route("/math/<int:num1>/<operation>/<int:num2>")
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
            return "Error: Division by zero"
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulo by zero"
    else:
        return "Error: Invalid operation"

    return f"{result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
