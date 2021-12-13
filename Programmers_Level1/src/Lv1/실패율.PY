n = 4
stages = [1, 1, 1, 1, 1]
totalplayer = len(stages)
answer = []
tmp = []
for i in range(1, n+1):
    cnt = 0
    for j in stages:
        if i == j:
            cnt += 1
    if cnt == 0:
        fail = 0
    else:
        fail = cnt/totalplayer
    totalplayer = totalplayer-cnt
    tmp.append((i, fail))
tmp.sort(key=lambda x: x[1], reverse=True)
for x in tmp:
    answer.append(x[0])
print(tmp)
