import sys

s = "AB"
s = list(s)
n = 1
for i in range(len(s)):
    if s[i].isupper():
        s[i] = chr((ord(s[i])-ord('A')+n) % 26+ord('A'))
    elif s[i].islower():
        s[i] = chr((ord(s[i])-ord('a')+n) % 26+ord('a'))
answer = ''.join(s)
print(answer)
