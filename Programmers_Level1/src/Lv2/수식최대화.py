# * + - 순일때

import copy

expression = "100-200*300-500+20"
chance = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'],
          ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]
now = ''
array = []
answer = -2147000000
for x in expression:
    if x != '*' and x != '+' and x != '-':
        now += x
    else:
        array.append(int(now))
        array.append(x)
        now = ''
array.append(int(now))
print(array)


for ch in chance:
    arrcopy = copy.deepcopy(array)
    for i in range(3):
        tmp = ch[i]  # tmp 는 *
        for j in range(0, len(arrcopy)-1):
            if tmp == arrcopy[j]:  # 1인덱스에 *있음
                left = arrcopy[j-1]
                right = arrcopy[j+1]
                if arrcopy[j] == '*':
                    arrcopy[j+1] = left*right
                elif arrcopy[j] == '+':
                    arrcopy[j+1] = left+right
                elif arrcopy[j] == '-':
                    arrcopy[j+1] = left-right
                arrcopy[j-1] = -1
                arrcopy[j] = -1
        a = []
        for x in arrcopy:
            if x != -1:
                a.append(x)
        arrcopy = copy.deepcopy(a)
    answer = max(answer, abs(arrcopy[0]))
print(answer)

# https://lastwinter.tistory.com/m/97 출처
