n=123

answer=0
while n>0:
  tmp=n%10
  n=n//10
  answer+=tmp
print(answer)