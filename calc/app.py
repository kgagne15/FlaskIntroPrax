# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def add_path():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = add(a, b)
#     return str(result)

# @app.route('/sub')
# def sub_path():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = sub(a, b)
#     return str(result)

# @app.route('/mult')
# def mult_path():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = mult(a, b)
#     return str(result)

# @app.route('/div')
# def div_path():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = div(a, b)
#     return str(result)

@app.route('/math/<type>')
def math_path(type):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if type == 'add':
        result = add(a, b)
    elif type == 'sub':
        result = sub(a, b)
    elif type == 'mult':
        result = mult(a, b)
    elif type == 'div':
        result = div(a, b)
    else:
        return 'this is not a valid entry'
    
    return str(result)
