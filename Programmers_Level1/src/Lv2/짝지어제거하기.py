s = 'abcda'

stack = []
for x in s:
    if stack:
        if x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    else:
        stack.append(x)
if stack:
    answer = 0
else:
    answer = 1

print(answer)
