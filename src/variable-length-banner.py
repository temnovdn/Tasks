# http://usingpython.com/python-programming-challenges/


def create_banner(string):
        banner_length = len(string) + 4
        print("*" * banner_length)
        print('* {} *'.format(string))
        print("*" * banner_length)

