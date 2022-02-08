

from collections import deque


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = len(maps)
m = len(maps[0])

q = deque()
q.append((0, 0))
dis = [[0]*n for _ in range(m)]
dis[0][0] = 1
# BFS
while q:
    tmp = q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if m > x >= 0 and n > y >= 0 and maps[y][x] == 1:
            if dis[x][y] == 0:
                dis[x][y] = dis[tmp[0]][tmp[1]]+1
                q.append((x, y))
if dis[-1][-1] == 0:
    answer = -1
else:
    answer = dis[-1][-1]

print(answer)

# DFS로 풀면안됨
