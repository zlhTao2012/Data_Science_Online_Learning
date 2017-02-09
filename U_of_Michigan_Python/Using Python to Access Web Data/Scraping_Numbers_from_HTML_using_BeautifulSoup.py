import urllib
from bs4 import BeautifulSoup
import re

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    nums = re.findall('[0-9]+', str(tag))
    for num in nums:
        sum += int(num)

print sum