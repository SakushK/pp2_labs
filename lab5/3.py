import re
txt=input()

if re.search('^[a-z]+_[a-z]+$',txt):
    print("ok")
else:
    print ("not ok")
