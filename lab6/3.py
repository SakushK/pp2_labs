word=input()

ans=format("It's palindrome!")

for i in range(len(word)-1):
    
    if word[i]!=word[len(word)-1-i]:
        
        ans="It is"+format(" not ")+format("palindrome")
        
        
print(ans)
