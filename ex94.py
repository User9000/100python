

#URL CLEANER

with open("urls.txt", "r") as fd:
    
    for i in fd:
        #print(i.replace("https", "http"))
        remove_s = i.replace("https","http")
        add_slash = remove_s.replace("/", "//")
        #print(i.replace("/","//"))
        print(add_slash)
