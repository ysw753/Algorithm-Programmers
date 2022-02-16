number = "1924"
k = 2

stk = []
for i in number:
    while stk and stk[-1] < i and k > 0:
        k -= 1
        stk.pop()
    stk.append(i)
answer = "".join(stk[:len(stk)-k])
print(answer)


# k = 1
# nth = 0
# length = len(number)
# tmp = []

# for _ in range(k):
#     for i in range(length-nth):
#         num = number[0:i]+number[i+1:]
#         if tmp:
#             if tmp[0] <= num:
#                 tmp.pop()
#                 tmp.append(num)
#         else:
#             tmp.append(num)
#     number = tmp[0]
#     tmp = []
#     nth += 1

# answer = ''.join(number)
# if len(answer):
#     print(answer)
# else:
#     print('0')


# for j in range(3):
#     print(tmp[0:j]+tmp[j+1:])
