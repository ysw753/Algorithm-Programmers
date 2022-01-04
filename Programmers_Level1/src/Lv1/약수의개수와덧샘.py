left = 24
right = 27
answer = 0


def getCountMeasure(num):
    cnt = 0
    for x in range(1, num+1):
        if num % x == 0:
            cnt += 1
    return cnt


for x in range(left, right+1):
    if getCountMeasure(x) % 2 == 0:
        answer += x
    else:
        answer -= x
print(answer)
