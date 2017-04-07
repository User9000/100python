'''
This alternative solution uses the built-in re  module which provides regular expression matching operations.
We're using the split method of that module and the expression ",| " is meant to replace commas with spaces. 
Using methods from the re  module can be more appropriate than Python built-in methods when string operations are complicated. However, 
for this simple scenario the re  module could be skipped.

'''



import re 

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(",| ", string)
        return len(string_list)

print(count_words_re("words1.txt"))

