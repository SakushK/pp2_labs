import re 
txt=input()

if re.search("^a(b*)$",txt):
    
    print ("yes")
else:
    print ("no")
