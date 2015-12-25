import random
import sys


def game():
    secret_array = [random.randint(0, 9) for n in xrange(0, 4)]
    secret = ''
    attempts = 0
    for digit in secret_array:
        secret += str(digit)
    verify_result = ''
    while verify_result != '****':
        digits = read_input()
        attempts += 1
        verify_result = verify_number(digits, secret)
        print('Guessed numbers: %s' % verify_result)
        if verify_result != '****':
            print('Wrong! Try one more time.')
    print('Congratulation! You won!')
    print('It took you %d attempts' % attempts)


def read_input():
    """Reads user input string, then verifies if it's four digits and returns it if verification is successful
    """
    input_numbers = ''
    while len(input_numbers) != 4:
        print('Please input four digits: ')
        input_numbers = sys.stdin.readline().rstrip('\n')
        if len(input_numbers) != 4:
            print('Please input FOUR digits.')
            input_numbers = ''
        for number in input_numbers:
            if not number.isdigit():
                print('Please input four DIGITS.')
                input_numbers = ''
                break
    return input_numbers


def verify_number(numbers, secret):
    """Compares 4 numbers in numbers string with digits and returns the quantity of digits
    matching with secret.
    :parameter numbers
    :parameter secret
    """
    result = ''
    for i in xrange(0, 4):
        if numbers[i] == secret[i]:
            result += '*'
    return result


if __name__ == "__main__":
    game()
