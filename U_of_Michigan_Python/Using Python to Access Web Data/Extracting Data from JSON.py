import json
import urllib


while True:

    address = raw_input('Enter url: ')
    if len(address) < 1 : break

    url = address
    print url
    uh = urllib.urlopen(url)
    input = uh.read()
    print 'Retrieved',len(input),'characters'
    #print data
    info = json.loads(input)
    print 'Count:', len(info)

    print json.dumps(info, indent=4)

    sum = 0

    for i in range(len(info['comments'])):
        sum += int(info['comments'][i]['count'])

    print 'Sum', sum

