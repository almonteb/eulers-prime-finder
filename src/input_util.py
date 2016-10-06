from responses import InvalidUsage


def intify(i):
    try:
        return int(i)
    except:
        raise InvalidUsage("Value {0} is not an integer".format(i))


def assert_valid_num_digits(i):
    if i > 12:
        raise InvalidUsage("{0} digits is too computationally expensive, try a bit lower".format(i))
