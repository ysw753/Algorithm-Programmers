dartResult = '1D2S3T*'

num = []
absnum = []
answer = 0
for x in dartResult:
    tmpnum = 0

    if x.isdecimal():
        if num:
            tennum = num.pop()
            tennum = int(tennum)*10
            num.append(int(x)+tennum)
        else:
            num.append(int(x))
    elif x == 'S':
        tmpnum = num.pop()
        tmpnum = tmpnum**1
        absnum.append(tmpnum)
    elif x == 'D':
        tmpnum = num.pop()
        tmpnum = tmpnum**2
        absnum.append(tmpnum)
    elif x == 'T':
        tmpnum = num.pop()
        tmpnum = tmpnum**3
        absnum.append(tmpnum)
    elif x == '*':
        if len(absnum) == 1:
            absnum[-1] = absnum[-1]*2
        elif len(absnum) > 1:
            absnum[-1] = absnum[-1]*2
            absnum[-2] = absnum[-2]*2
    elif x == '#':
        absnum[-1] = absnum[-1]*(-1)
for x in absnum:
    answer += x
print(answer)
