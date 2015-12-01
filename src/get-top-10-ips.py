import re
from collections import Counter

filepath = raw_input('Log file path: ')

opened_file = open(str(filepath), mode='r')
content = opened_file.readlines()

list_ips = []
for line in content:
    if re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line):
        ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).string.rstrip('\n')
        list_ips.append(ip)

top_ten = Counter(list_ips).most_common(10)

for item in top_ten:
    print(item)
