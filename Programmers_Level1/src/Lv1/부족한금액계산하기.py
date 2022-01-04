import sys

price = 3
money = 20
count = 4
total = 0
tmp = 0
while count > 0:
    tmp = tmp+price
    total += tmp
    count -= 1

answer = total-money
if answer <= 0:
    answer = 0
print(answer)
