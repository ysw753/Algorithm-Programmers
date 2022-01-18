s = "abcabcabcabcdededededede"
length = 2147000000
answer = ''
# if len(s)==1:
#   return 1
for i in range(1, len(s)//2+1):
    cnt = 1
    tmp = s[:i]
    for j in range(i, len(s)+1, i):
        if tmp == s[j:i+j]:
            cnt += 1
        else:
            if cnt > 1:
                answer += str(cnt)+tmp
            else:
                answer += tmp
            cnt = 1
            tmp = s[j:i+j]
    if cnt == 1:
        answer += tmp
    print(len(answer))
    if length > len(answer):
        length = len(answer)
    answer = ''
