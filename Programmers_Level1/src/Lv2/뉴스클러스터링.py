

import sys
from unittest import result

str1 = 'A+C'
len1 = len(str1)

str2 = 'DEF'
len2 = len(str2)

str1list = []
str2list = []

for i in range(len1-1):
    str = str1[i:i+2]
    for s in str:
        if not(s.isalpha()):
            break
    else:
        str1list.append(str)


for i in range(len2-1):
    str = str2[i:i+2]
    for s in str:
        if not(s.isalpha()):
            break
    else:
        str2list.append(str)
realstr1list = []
realstr2list = []

for x in str1list:
    tmp = ''
    tmp += x.upper()
    realstr1list.append(tmp)
for x in str2list:
    tmp = ''
    tmp += x.upper()
    realstr2list.append(tmp)


# 여기서부터 다중집합을 구현해야함
icopy1 = realstr1list.copy()
icopy2 = realstr2list.copy()

# 교집합
inter = []
for i in icopy1:
    if i in icopy2:
        icopy2.remove(i)
        inter.append(i)

a_temp = realstr1list.copy()
a_result = realstr1list.copy()

for i in realstr2list:
    if i not in a_temp:
        a_result.append(i)
    else:
        a_temp.remove(i)

b_temp = realstr2list.copy()
b_result = realstr2list.copy()

for i in realstr1list:
    if i not in b_temp:
        b_result.append(i)
    else:
        b_temp.remove(i)
union = inter+a_temp+b_temp

if len(inter) == 0 and len(union) == 0:
    answer = 1*65536
else:
    answer = int(len(inter)/len(union)*65536)
print(answer)
