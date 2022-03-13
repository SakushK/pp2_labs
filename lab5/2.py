import re
txt=input()

if re.search("ab{2,3}",txt): 
    
    print("yes")
else: 
    print ("no")
    
    
