s = " try hello world"

words = s.split(" ")

answer = []
for x in words:
    tmp = ''
    for i in range(len(x)):
        if i == 0 or i % 2 == 0:
            tmp += x[i].upper()
        else:
            tmp += x[i].lower()
    answer.append(tmp)
answer = ' '.join(answer)
print(answer)
