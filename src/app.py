from io import TextIOWrapper
from flask import Flask, render_template, jsonify, request
from responses import Response, InvalidUsage
import math_util
import input_util
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/')
def index():
    '''Renders the single page'''
    return render_template('home.html')


@app.route('/single', methods=['POST'])
def process_single():
    '''Handles requests for the single submit form. 
    Also accepts a POST request with JSON data in the format of:
    { 
        'x': 3,
        'y': 3,
    }
    '''
    x = input_util.intify(request.json['x'])
    y = input_util.intify(request.json['y'])
    return process_response(({'xth': x, 'num_digits': y},))


@app.route('/multiple', methods=['POST'])
def process_multiple():
    '''Handles requests for the multi submit file upload form. 
    Expects a single form field, named 'file' with a 2 column CSV as its contents. Ex.
    1,2
    3,4
    5,6
    '''
    # wraps the file stream in a TextIOWrapper to allow for line-by-line consumption
    file = TextIOWrapper(request.files['file'].stream)
    inputs = []
    while True:
        line = file.readline()
        if not line:
            # last line in the file
            break
        # build x,y pairs and ensure they're integers
        x, y = [input_util.intify(c) for c in line.split(',')]
        inputs.append({'xth': x, 'num_digits': y})
    return process_response(inputs)


def process_response(inputs):
    ''' Iterates through all the prime requests, processes, & creates a JSON response for the client'''
    primes = []
    for input in inputs:
        logging.info("Computing xth: {0}, num_digits: {1}".format(input['xth'], input['num_digits']))
        input_util.assert_valid_num_digits(input['num_digits'])
        primes.append(math_util.find_xth_prime(input['xth'], input['num_digits']))
    return jsonify(Response(primes).serialize())


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    '''Handler for InvalidUsage ex. These are for 'handled' exceptions'''
    return jsonify(Response(error=error.message).serialize()), error.status_code


@app.errorhandler(Exception)
def handle_unknown_error(error):
    '''Handle any other exception that may get caughed up due to misuse of APIs/external libs, etc.'''
    # since we're handling (swallowing) the ex, lets print it
    logging.exception(error)
    return jsonify(Response(error=str(error)).serialize()), 500


if __name__ == '__main__':
    app.run(debug=True)
