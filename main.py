from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result

@app.route('/sub')
def substraction():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1-value2
    return '%d \n' % result

@app.route('/mult')
def multiplication():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1*value2
    return '%d \n' % result

@app.route('/div')
def division():
    value1=request.args.get('A',default = 0, type = float)
    value2=request.args.get('B',default = 0, type = float)
    result=value1/value2
    return '%.2f \n' % result 

@app.route('/radd')
def r_addition():
    value1=request.args.get('A',default = 0, type = str)
    num1,den1 = str(value1).split('/')
    value2=request.args.get('B',default = 0, type = str)
    num2,den2 = str(value2).split('/')
    result=str(Fraction(int(num1),int(den1))+Fraction(int(num2),int(den2)))
    return result

@app.route('/rsub')
def r_subtraction():
    value1=request.args.get('A',default = 0, type = str)
    num1,den1 = str(value1).split('/')
    value2=request.args.get('B',default = 0, type = str)
    num2,den2 = str(value2).split('/')
    result=str(Fraction(int(num1),int(den1))-Fraction(int(num2),int(den2)))
    return result

@app.route('/rmult')
def r_multiplication():
    value1=request.args.get('A',default = 0, type = str)
    num1,den1 = str(value1).split('/')
    value2=request.args.get('B',default = 0, type = str)
    num2,den2 = str(value2).split('/')
    result=str(Fraction(int(num1),int(den1))*Fraction(int(num2),int(den2)))
    return result 

@app.route('/rdiv')
def r_division():
    value1=request.args.get('A',default = 0, type = str)
    num1,den1 = str(value1).split('/')
    value2=request.args.get('B',default = 0, type = str)
    num2,den2 = str(value2).split('/')
    result=str(Fraction(int(num1),int(den1))/Fraction(int(num2),int(den2)))
    return result


if __name__ == "__main__":
    app.run()
