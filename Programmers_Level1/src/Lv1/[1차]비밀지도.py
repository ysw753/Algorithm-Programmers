from collections import deque


n=6
arr1=	[46, 33, 33 ,22, 31, 50]
arr2=	[27 ,56, 19, 14, 14, 10]

mapA=[]
mapB=[]
answer=[]
for i in range(n):
  tmp=arr1[i]
  tmplist=deque()
  while tmp>0:
    x=tmp%2
    tmp=tmp//2
    tmplist.appendleft(x)
  while len(tmplist)!=n:
    tmplist.appendleft(0)
  mapA.append(list(tmplist))
print(mapA)

for i in range(n):
  tmp=arr2[i]
  tmplist=deque()
  while tmp>0:
    x=tmp%2
    tmp=tmp//2
    tmplist.appendleft(x)
  while len(tmplist)!=n:
    tmplist.appendleft(0)
  mapB.append(list(tmplist))
print(mapB)
for i in range(n):
  for j in range(n):
    if mapA[i][j]==1:
      mapB[i][j]=1

for i in range(n):
  tmplist=''
  for j in range(n):
    if mapB[i][j]==1:
      tmplist+='#'
    elif mapB[i][j]==0:
      tmplist+=' '
  answer.append(tmplist)
print(mapB)
print(answer)



