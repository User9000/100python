

#URL CLEANER

with open("urls.txt", "r") as fd:
    
    for i in fd:
       
        remove_s = i.replace("https","http")
        add_slash = remove_s.replace("/", "//")
        
        print(add_slash)
