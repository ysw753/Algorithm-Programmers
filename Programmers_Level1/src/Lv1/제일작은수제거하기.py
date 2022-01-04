arr=[4,3,2,1]

min=2147000000
answer=[]
if len(arr)==0 or len(arr)==1 and arr[0]==10:
  answer.append(-1)
else:
  for x in arr:
    if x<min:
      min=x
  for x in arr:
    if x!=min:
      answer.append(x)
print(answer)

