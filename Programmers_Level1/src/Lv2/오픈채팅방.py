record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
dic = {}
answer = []
for x in record:
    x_split = x.split()
    if len(x_split) == 3:
        dic[x_split[1]] = x_split[2]


for x in record:
    x_split = x.split()
    if x_split[0] == 'Enter':
        key = x_split[1]
        answer.append('%s님이 들어왔습니다.' % dic[key])
    elif x_split[0] == 'Leave':
        key = x_split[1]
        answer.append('%s님이 나갔습니다.' % dic[key])
print(answer)
