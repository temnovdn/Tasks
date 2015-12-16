import re
import string
from functools import wraps
from time import time
from memory_profiler import memory_usage

PATTERN = r'^[a-zA-Z](\w|\d|\.|\-){0,18}[a-zA-Z0-9]$|^[a-zA-Z0-9]$'


def measure_time_and_memory(function):
    """Prints function execution time
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


@measure_time_and_memory
def verify_login_regexp(login, pattern):
    """Verifies login string with python re library and returns True if it matches
     python regexp pattern
    Returns False otherwise.
    :parameter login
    :parameter pattern
    """
    result = re.match(pattern, login)
    if result == None:
        return False
    else:
        return True


@measure_time_and_memory
def verify_login_if_else(login):
    """Verifies login string by trying some if-else conditions and returns True if it matches
    python regexp pattern ^[a-zA-Z](\w|\d|\.|\-){0,19}[a-zA-Z]$|^[a-zA-Z0-9]$
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

# Verifying valid login strings
print('Verifying valid login strings')
print('Regexp: {}'.format(verify_login_regexp('Some.LogIn12_totest1', PATTERN)))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn12_totest1')))
# Too long strings
print('Too long strings')
print('Regexp: {}'.format(verify_login_regexp('Some.LogIn123_totest123123123', PATTERN)))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn123_totest123123123')))
# One letter string
print('One letter string')
print('Regexp: {}'.format(verify_login_regexp('S', PATTERN)))
print('If else: {} \n'.format(verify_login_if_else('S')))
# String with unallowed symbol in the end
print('String with unallowed symbol in the end')
print('Regexp: {}'.format(verify_login_regexp('Some.LogIn12_totest_', PATTERN)))
print('If else: {} \n'.format(verify_login_if_else('Some.LogIn12_totest_')))
# String with unallowed symbol in the beginning
print('String with unallowed symbol in the end')
print('Regexp: {}'.format(verify_login_regexp('1ome.LogIn12_totest1', PATTERN)))
print('If else: {} \n'.format(verify_login_if_else('1ome.LogIn12_totest1')))

print('If/else version is slightly faster than regexp version')


