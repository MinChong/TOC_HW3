# -*- coding: utf-8 -*-

'''
program : TocHW3.py
Name : 黃崇珉
Student ID : F74006250
Description : Parsing the information    
'''
import json
import urllib2
import sys
import re

if len(sys.argv) != 5:
    print 'Too few argument'
    sys.exit(0)
'''
if type(int(sys.argv[4])) != int: 
    print 'Year should be integer.'
    sys.exit(0)
'''
try:
    int(sys.argv[4])
except ValueError as e:
    print e
    sys.exit(0)
    

#jsonSource = urllib.urlopen(sys.argv[1])
request = urllib2.Request(sys.argv[1])
  
try:
    jsonSource = urllib2.urlopen(request)
except (ValueError, urllib2.URLError) as e:
    print e
    sys.exit(0)

regexp = re.compile(r"{\"鄉鎮市區\":\"(?P<region>[^\"]+)\",[^,]+,\"土地區段[^\:]+:\"(?P<location>[^\"]+)\","
					r"([^,]+,)+\"交易年月\":(?P<date>[0-9]+),([^,]+,)+\"總價元\":(?P<price>[0-9]+)")

totalPrice = 0;
match = 0;
for line in jsonSource.readlines():
	result = regexp.match(line)
	if result:
		region = result.group('region')
		if region == sys.argv[2]:
			location = result.group('location')
			road = location.find(sys.argv[3])
			#print road
			if road != -1:
				date = result.group('date')
				if date[0:3]>=sys.argv[4]:
					price = result.group('price')
					totalPrice = totalPrice + int(result.group('price'))
					match = match + 1;
					#print region + "   " + location + "   " + date + "   " + price					

if match != 0:
    avg_price = totalPrice / match
    print("%d" %(avg_price))
else:
    print('Not found.')
jsonSource.close()

