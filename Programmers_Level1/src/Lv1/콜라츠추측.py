num = 626331
trial = 500
answer = 0
while trial > 0:
    if num == 1:
        break
    if num % 2 == 0:
        num = num/2
        answer += 1
    else:
        num = num*3+1
        answer += 1
    trial -= 1
if trial == 0:
    answer = -1
print(answer)
