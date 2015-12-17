import re
from collections import Counter
from optparse import OptionParser

parser = OptionParser(usage='usage: [-f <file>][--file <file>]')
parser.add_option('-f', '--file', dest='file', help='Path to file')
(options, args) = parser.parse_args()

file_path = vars(options).get('file')

def parse_log(file_name):
    with open(str(file_name), mode='r') as opened_file:
        not_stripped_content = opened_file.readlines()
        content = [line.rstrip('\n') for line in not_stripped_content]

    return Counter(content).items()

counted = parse_log(file_path)

for item in counted:
    print('Word: %s, count: %s' % item)
