def reverse_word(s):
    
   words = s
   words = list(reversed(words))
   
   print(" ".join(words))

s=input().split()
reverse_word(s)
