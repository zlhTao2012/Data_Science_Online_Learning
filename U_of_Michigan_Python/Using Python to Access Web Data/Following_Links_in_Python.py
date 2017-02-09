import urllib
from bs4 import BeautifulSoup
import re

url = raw_input('Enter Url: ')
count = int(raw_input('Enter Count: '))
position = int(raw_input('Enter position: '))

i = 0

while i < count:

    print "Retrieving:" + url

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    name_list = list()

    # Retrieve all of the anchor tags
    tags = soup('a')

    i += 1

    for tag in tags:
        Tag = str(tag)
        name = re.findall('.+>(.*)<', Tag)
        name_list.append(name)
        url = tag.get('href', None)

        if len(name_list) == position:

            print name_list[position-1]
            print url
            break


