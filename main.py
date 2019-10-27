  
from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)


def take_inputs():
    input1 = request.args.get('X', default=0, type=str)
    try:
        input1 = Fraction(input1)
    except ZeroDivisionError:
        return "X's denominator shouldn't be zero! \n"
    except ValueError:
        return "X's value should be a number (includes fraction, float, integer). \n"
    input2 = request.args.get('Y', default=0, type=str)
    try:
        input2 = Fraction(input2)
    except ZeroDivisionError:
        return "Y's denominator shouldn't be zero! \n"
    except ValueError:
        return "Y's value should be a number (includes fraction, float, integer). \n"
    return input1, input2


@app.route('/')
def index():
    return 'Usage;\n<Operation>?X=<Input1>&Y=<Input2>\n'

@app.route('/add')
def addition():
    try:
        input1, input2 = take_inputs()
        result = input1 + input2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


@app.route('/sub')
def subtraction():
    try:
        input1, input2 = take_inputs()
        result = input1 - input2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


@app.route('/mul')
def multiplication():
    try:
        input1, input2 = take_inputs()
        result = input1 * input2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


@app.route('/div')
def division():
    try:
        input1, input2 = take_inputs()
        try:
            result = ((input1)/(input2))
        except ZeroDivisionError:
            warning_msg = "Y's value shouldn't be zero! \n"
            return warning_msg
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


if __name__ == "__main__":
    app.run()
