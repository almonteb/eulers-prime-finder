from responses import InvalidUsage


def intify(i):
    ''' returns the int representation of i, otherwise raises an InvalidUsage ex'''
    try:
        return int(i)
    except:
        raise InvalidUsage("Value {0} is not an integer".format(i))


def assert_valid_num_digits(i):
    ''' asserts the number of digit complexity is 12 or under, otherwise raises an InvalidUsage ex'''    
    if i > 12:
        raise InvalidUsage("{0} digits is too computationally expensive, try a bit lower".format(i))
