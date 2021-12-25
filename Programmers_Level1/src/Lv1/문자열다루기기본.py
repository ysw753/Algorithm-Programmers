s = '1234'
for x in s:
    if len(s) != 4 and len(s) != 6:
        answer = False
        break
    if x.isalpha():
        answer = False
        break
else:
    answer = True
print(answer)
