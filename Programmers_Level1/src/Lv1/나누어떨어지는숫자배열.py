arr = [5, 9, 7, 10]
divisor = 5
answer = []
for x in arr:
    if int(x) % divisor == 0:
        answer.append(x)
if answer:
    answer.sort()
else:
    answer.append(-1)
print(answer)
