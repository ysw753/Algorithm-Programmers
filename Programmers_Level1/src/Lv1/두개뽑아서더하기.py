numbers = [0, 0, 0, 1]

answer = []
ch = [0]*len(numbers)


def DFS(L, sum):
    if L == 2:
        answer.append(sum)
    else:
        for i in range(len(numbers)):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L+1, sum+numbers[i])
                ch[i] = 0


DFS(0, 0)
answer = set(answer)
answer = list(answer)
answer.sort()
print(answer)
