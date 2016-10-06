class Response(object):
    def __init__(self, primes=[], error=None):
        self.error = error
        self.primes = primes

    def serialize(self):
        return {
            'error': self.error,
            'primes': [prime.__dict__ for prime in self.primes],
        }


class Prime(object):
    def __init__(self, xth, num_digits, prime, pos):
        self.xth = xth
        self.num_digits = num_digits
        self.prime = prime
        self.pos = pos


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
