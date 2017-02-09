import urllib
import xml.etree.ElementTree as ET

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    tree = ET.fromstring(data)


    results = tree.findall('comments/comment')
    print'Count:', len(results)

    Sum = 0

    for comment in results:
        Sum += int(comment.find('count').text)

    print 'Sum: ', str(Sum)
