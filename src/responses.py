class Response(object):
    '''Default API response object. All responses should be of this type.'''
    def __init__(self, primes=[], error=None):
        self.error = error
        self.primes = primes

    def serialize(self):
        return {
            'error': self.error,
            'primes': [prime.__dict__ for prime in self.primes],
        }


class Prime(object):
    '''Object representing a prime as well as its position'''
    def __init__(self, xth, num_digits, prime, pos):
        self.xth = xth
        self.num_digits = num_digits
        self.prime = prime
        self.pos = pos


class InvalidUsage(Exception):
    '''Exception raised for invalid input -- contains a message with the reason'''
    status_code = 400

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
