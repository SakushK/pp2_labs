import re
txt=input()

if re.search("[A-Z]+[a-z]+$",txt):
    
    print("ok")
else:
    print("not ok")
    
