import math

answer = 0
N = 8
A = 4
B = 7

while A != B:
    answer += 1
    A, B = (A+1)//2, (B+1)//2
print(answer)
# length = N//2
# cnt = 1
# while(N >= 1):
#     if abs(A-B) == 1:
#         for i in range(length):
#             if (A+B) == 3+(4*i):
#                 answer = cnt
#                 break
#     A = math.ceil(A/2)
#     B = math.ceil(B/2)
#     cnt += 1
#     N = N/2
# print(answer)
