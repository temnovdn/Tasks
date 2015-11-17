import re
import string

def verify_login_regexp(login):
    """Verifies login string with python re library and returns True if it matches
     python regexp pattern ^[a-zA-Z](\w|\d|\.|\-){0,19}[a-zA-Z0-9]+$
    Returns False otherwise.
    """
    pattern = "^[a-zA-Z](\w|\d|\.|\-){0,19}[a-zA-Z0-9]+$"
    result = re.search(pattern, login)
    if result == None:
        return False
    else:
        return True

def verify_login_if_else(login):
    """Verifies login string by trying some if-else conditions and returns True if it matches
    python regexp pattern ^[a-zA-Z](\w|\d|\.|\-){0,19}[a-zA-Z0-9]+$
    Returns False otherwise.
    """
    alphabetical = string.ascii_letters
    numeric = "01234567890"
    symbol = ".-_"
    alphanumeric = alphabetical + numeric
    allowed = alphanumeric + symbol

    result = True

    first = login[0]
    last = login[-1]

    if first in alphabetical:
        if last in alphanumeric:
            for char in login[1:-1]:
                if not (char in allowed):
                    result = False
        else:
            result = False
    else:
        result = False

