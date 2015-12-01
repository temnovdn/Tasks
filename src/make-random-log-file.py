import random
file_to_write = open('resources/shuffled_data', mode='w')

ips = []
for i in range(0, 100):
    ip = str(random.randint(0, 255)) + '.' +\
         str(random.randint(0, 255)) + '.' +\
         str(random.randint(0, 255)) + '.' +\
         str(random.randint(0, 255)) + '\n'

    ips.append(ip)

log = []

for i in range(500, random.randint(500, 1000)):
    log.append(random.choice(ips))

file_to_write.writelines(log)
