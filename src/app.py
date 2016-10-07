from io import TextIOWrapper
from flask import Flask, render_template, jsonify, request
from responses import Prime
import input_util
import math_util
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
    inputs = ({'xth': request.json['x'], 'num_digits': request.json['y']},)
    return jsonify([prime.__dict__ for prime in process_primes(inputs)])


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
        x, y = [c for c in line.split(',')]
        inputs.append({'xth': x, 'num_digits': y})
    return jsonify([prime.__dict__ for prime in process_primes(inputs)])


def process_primes(inputs):
    ''' Iterates through all the prime requests, checks for validity, processes, & creates a JSON response for the client'''
    primes = []
    for input in inputs:
        logging.info("Computing xth: {0}, num_digits: {1}".format(input['xth'], input['num_digits']))
        if input_util.is_int(input['xth']):
            input['xth'] = int(input['xth'])
        else:
            primes.append(Prime(input['xth'], input['num_digits'],
                                error="{0} is an invalid value for X".format(input['xth'])))
            continue

        if input_util.is_int(input['num_digits']):
            input['num_digits'] = int(input['num_digits'])
        else:
            primes.append(Prime(input['xth'], input['num_digits'],
                                error="{0} is an invalid value for Y".format(input['num_digits'])))
            continue

        if input['num_digits'] > 12:
            primes.append(Prime(input['xth'], input['num_digits'],
                                error="{0} digits is too computationally expensive, try a bit lower".format(input['num_digits'])))
            continue

        primes.append(math_util.find_xth_prime(input['xth'], input['num_digits']))
    return primes


@app.errorhandler(Exception)
def handle_unknown_error(error):
    '''Handle any other exception that may get caughed up due to misuse of APIs/external libs, etc.'''
    # since we're handling (swallowing) the ex, lets print it
    logging.exception(error)
    return jsonify({'error': str(error)}), 500


if __name__ == '__main__':
    app.run(debug=True)
