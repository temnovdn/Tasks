import re
import regex
import string
from functools import wraps
from time import time

PATTERN = r'^[a-zA-Z](\w|\d|\.|\-){0,18}[a-zA-Z0-9]$|^[a-zA-Z0-9]$'


def measure_time(function):
    """Prints function execution time.
    :param function
    """
    @wraps(function)
    def wrapper(*args, **kwds):
        start = time()
        result = function(*args, **kwds)
        elapsed = time() - start
        print('Function %s took %s time to execute'%(function.__name__, elapsed))
        return result
    return wrapper


@measure_time
def verify_login_re(pattern, login):
    """Matches login string with regexp pattern, using re module from python standard library and returns True if it matches
    Returns False otherwise.
    :parameter login
    :parameter pattern
    """
    result = re.match(pattern, login)
    if result is None:
        return False
    else:
        return True


@measure_time
def verify_login_if_else(login):
    """Matches login string with login pattern (regexp: '^[a-zA-Z](\w|\d|\.|\-){0,18}[a-zA-Z0-9]$|^[a-zA-Z0-9]$')
    by trying some if-else conditions and returns True if it matches.
    Returns False otherwise.
    :parameter login
    """
    alphabetical = string.ascii_letters
    numeric = "01234567890"
    symbol = ".-_"
    alphanumeric = alphabetical + numeric
    allowed = alphanumeric + symbol

    result = True

    first = login[0]
    last = login[-1]
    length = len(login)

    if length <= 20:
        if first in alphabetical:
            if last in alphanumeric:
                for char in login[1:-1]:
                    if not (char in allowed):
                        result = False
                        break
            else:
                result = False
        else:
            result = False
    else:
        result = False

    return result


@measure_time
def verify_login_regex(pattern, login):
    """Matches login string with pattern, using regex library (https://pypi.python.org/pypi/regex)
    and returns True if it matches.
     python regexp pattern
    Returns False otherwise.
    :parameter login
    :parameter pattern
    """
    result = regex.match(pattern, login)
    if result is None:
        return False
    else:
        return True

# Code to measure execution time of various versions
# Verifying valid login strings
print('Verifying valid login strings')
print('Re: {}'.format(verify_login_re(PATTERN, 'Some.LogIn12_totest1')))
print('Regex: {}'.format(verify_login_regex(PATTERN, 'Some.LogIn12_totest1')))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn12_totest1')))
# Too long strings
print('Too long strings')
print('Re: {}'.format(verify_login_re(PATTERN, 'Some.LogIn123_totest123123123')))
print('Regex: {}'.format(verify_login_regex(PATTERN, 'Some.LogIn123_totest123123123')))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn123_totest123123123')))
# One letter string
print('One letter string')
print('Re: {}'.format(verify_login_re(PATTERN, 'S')))
print('Regex: {}'.format(verify_login_regex(PATTERN, 'S')))
print('If else: {} \n'.format(verify_login_if_else('S')))
# String with unallowed symbol at the end
print('String with unallowed symbol in the end')
print('Re: {}'.format(verify_login_re(PATTERN, 'Some.LogIn12_totest_')))
print('Regex: {}'.format(verify_login_regex(PATTERN, 'Some.LogIn12_totest_')))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn12_totest_')))
# String with unallowed symbol at the beginning
print('String with unallowed symbol in the beginning')
print('Re: {}'.format(verify_login_re(PATTERN, '1ome.LogIn12_totest1')))
print('Regex: {}'.format(verify_login_regex(PATTERN, '1ome.LogIn12_totest1')))
print('If else: {} \n'.format(verify_login_if_else('1ome.LogIn12_totest1')))
