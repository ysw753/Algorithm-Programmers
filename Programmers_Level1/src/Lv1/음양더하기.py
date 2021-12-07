import sys
sys.stdin = open("input.txt", 'r')

absolutes = [4, 7, 12]
signs = [True, False, True]
result = 0
for i in range(len(signs)):
    if signs[i]:
        result += absolutes[i]
    else:
        result += -(absolutes[i])

print(result)
