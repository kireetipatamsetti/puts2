from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
	return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'

@app.route('/div')
def division():
    try:
        a=request.args.get('A',default = 0, type = int)
    except ZeroDivisionError as e:
        a='None'
    try:
        b=request.args.get('B',default = 0, type = int)
    except ZeroDivisionError as e:
        b='None'
    if a == 'None' or b == 'None' :
        return 'None'
    else:
	try:
		result = a / b
		return str(round(float(result),3)) + "\n"
	except ZeroDivisionError as e:
	        return "b shouldn't be zero!" + "\n"
if __name__ == "__main__":
    app.run()



