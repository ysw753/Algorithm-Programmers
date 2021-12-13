import sys

d=[2,2,3,3]
budget = 10
d.sort()
sum=0
cnt=0
for x in d:
  sum+=x
  if sum<=budget:
    cnt+=1
  else:
    break
print(cnt)


# 시간초과남
# cnt=0
# cnt=0
# answer = 0
# def DFS(L,sum):
#         global cnt
#         global answer
#         if sum>budget:
#           return
#         if L==len(d):
#             if budget>=sum:
#                 if answer<cnt:
#                     answer=cnt
#         else:
#             cnt+=1
#             DFS(L+1,sum+d[L])
#             cnt-=1
#             DFS(L+1,sum)
# DFS(0,0)
# print(answer)