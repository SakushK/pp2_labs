s=input()

st=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        st.append(s[i])
        continue
    
    if (s[i]==')' or s[i]=='}' or s[i]==']') and st:
        if (st[-1]+s[i]=='()') or (st[-1]+s[i]=='{}') or (st[-1]+s[i]=='[]'):
            st.pop()
        else:
            print('No')
            exit()
   
if st==[]:
    print('Yes')
else:
    print('No')
