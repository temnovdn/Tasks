import re
from collections import Counter
from optparse import OptionParser

IP_PATTERN = r'((1\d{1,2}\.|\d\.|\d{2}\.|2[0-4]\d\.|25[0-5]\.){3}(25[0-5]|2[0-4]\d|1\d{1,2}|\d{2}|\d){1})+'

parser = OptionParser(usage='usage: [-f <log file>][--file <log file>]')
parser.add_option('-f', '--file', dest='file', help='Path to log file')
(options, args) = parser.parse_args()

file_path = vars(options).get('file')


def parse_log(file_name):
    with open(str(file_name), mode='r') as opened_file:
        content = opened_file.read()

    list_found = re.findall(IP_PATTERN, content)
    list_ips = []
    for item in list_found:
        list_ips.append(item[0])

    top_ten = Counter(list_ips).most_common(10)
    return top_ten

top = parse_log(file_path)

for item in top:
    print(item)
