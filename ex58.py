import json

from pprint import pprint

file = open("/Users/Carlo/Documents/100python/company2.json",'r+')

#the read function will throw the pointer to end of the file.
#the loads functioin will convert string into a dictionary
parsed_jason = json.loads(file.read())


#this will add the item to the employees section
parsed_jason['employees'].append({"firstName":"elias",
                                    "lastName":"mireles"})
#get the pointer to the beginning again.
file.seek(0)
#store the dictionary into a json file from the beginning.
json.dump(parsed_jason,file, indent=4, sort_keys=True)
