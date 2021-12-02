numbers=[1,2,3,4,6,7,8,0]
num=[0,1,2,3,4,5,6,7,8,9]
result=0
for x in num:
  if x not in numbers:
    result+=x
print(result)