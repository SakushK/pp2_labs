def palindrome(s):
    
    alternative = ''.join(reversed(s))
    
    if (s == alternative):
        return True
    return False

str=input()

if (palindrome(str)==True):
    
    print("True")
    
else:
    print("False")
