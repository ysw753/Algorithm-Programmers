numbers = [1, 1, 1, 1, 1]
total = 0
target = 3
cnt = 0


def DFS(L, total):
    global cnt

    if L == len(numbers):
        if total < 1:
            return
        if total == target:
            cnt += 1
    else:
        DFS(L+1, total+numbers[L])
        DFS(L+1, total-numbers[L])


DFS(0, 0)
print(cnt)
