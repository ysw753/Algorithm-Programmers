import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = []
maxx = math.ceil((100-progresses[0])/speeds[0])
cnt = 1
for i in range(1, len(progresses)):
    if maxx >= math.ceil((100-progresses[i])/speeds[i]):
        cnt += 1
    else:
        answer.append(cnt)
        cnt = 1
        maxx = math.ceil((100-progresses[i])/speeds[i])
answer.append(cnt)
print(answer)
