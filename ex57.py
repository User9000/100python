import json

from pprint import pprint
file = open("/Users/Carlo/Documents/100python/company2.json",'r')
parsed_jason = json.loads(file.read())

pprint(parsed_jason)