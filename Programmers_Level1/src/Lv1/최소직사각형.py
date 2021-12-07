


size=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

answer=0
first=0
second=0
for x in size:
  maxx=max(x[0],x[1])
  if maxx>first:
    first=maxx


for x in size:
  minn=min(x[0],x[1])
  if second<minn:
      second=minn
answer=first*second      
print(first)
print(second)
print(answer)

