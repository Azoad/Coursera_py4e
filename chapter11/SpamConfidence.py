"""find maximum spam confidence"""

import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    if len(stuff) != 1:
        continue

    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))
