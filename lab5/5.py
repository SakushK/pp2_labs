import re
txt=input()

if re.search("^a.*b$",txt):
    
    print("ok")
else:
    print("not ok")
