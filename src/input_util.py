def is_int(i):
    ''' returns true if i is an int, otherwise false'''
    try:
        int(i)
        return True
    except (ValueError, TypeError):
        return False
