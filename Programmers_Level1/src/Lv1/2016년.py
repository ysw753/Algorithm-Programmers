day=['THU','FRI','SAT','SUN','MON','TUE','WED']
month=[31,29,31,30,31,30,31,31,30,31,30,31]

a=5
b=24
totalDay = 0
for i in range(a-1):
  totalDay += month[i]
totalDay+=b

print(day[totalDay%7])
