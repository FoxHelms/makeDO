
class NotIntegerError(ValueError): pass


def determine(n):
    if not isinstance(n, int):
        raise NotIntegerError('n must be an integer!')
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'
    

determine('tree')