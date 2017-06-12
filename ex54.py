
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
    {"firstName": "Anna", "lastName": "Smith"},
    {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
    {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"][1]["lastname"] = "AQUII<=="

d["employees"].append({"firstName":"Carlo", "lastname": "lam"})

#d['owners'].update({'firstnName': 'Ferny', 'lastName': 'Queens'})

print(type(d))