class Prime(object):
    '''Object representing a prime as well as its position'''
    def __init__(self, xth, num_digits, prime=None, pos=None, error=None):
        self.xth = xth
        self.num_digits = num_digits
        self.prime = prime
        self.pos = pos
        self.error = error


class InvalidUsage(Exception):
    '''Exception raised for invalid input -- contains a message with the reason'''
    status_code = 400

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
