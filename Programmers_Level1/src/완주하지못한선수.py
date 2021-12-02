import sys
sys.stdin = open("input.txt", 'r')

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
dict = {}
result = ''
for x in participant:
    dict[x] = dict.get(x, 0)+1

for x in completion:
    if x in dict.keys():
        dict[x] -= 1

for key, val in dict.items():
    if val != 0:
        result += key
print(result)
