from collections import deque


s = "[](){}"
s = deque(s)
cnt = 0
tmparr = [0]

for x in s:
    if x == ']' and tmparr[-1] == '[':
        tmparr.pop()
    elif x == '}' and tmparr[-1] == '{':
        tmparr.pop()
    elif x == ')' and tmparr[-1] == '(':
        tmparr.pop()
    else:
        tmparr.append(x)
if len(tmparr) == 1:
    cnt += 1
tmparr = [0]
for i in range(1, len(s)):
    s.append(s.popleft())
    tmparr = [0]
    for x in s:
        if x == ']' and tmparr[-1] == '[':
            tmparr.pop()
        elif x == '}' and tmparr[-1] == '{':
            tmparr.pop()
        elif x == ')' and tmparr[-1] == '(':
            tmparr.pop()
        else:
            tmparr.append(x)
    if len(tmparr) == 1:
        cnt += 1
print(cnt)
