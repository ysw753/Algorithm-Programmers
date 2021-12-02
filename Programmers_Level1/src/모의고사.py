from collections import deque
import sys
sys.stdin = open("input.txt", 'r')

answers = [1, 3, 2, 4, 2]
m1 = {
    "omr": [1, 2, 3, 4, 5],
    "cnt": 0,
}
m2 = {
    "omr": [2, 1, 2, 3, 2, 4, 2, 5],
    "cnt": 0,
}
m3 = {
    "omr": [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    "cnt": 0,

}
i = 0
j = 0
k = 0
for x in answers:
    if i == len(m1["omr"]):
        i = 0
    if m1["omr"][i] == x:
        m1["cnt"] += 1
    i += 1

    if j == len(m2["omr"]):
        j = 0
    if m2["omr"][j] == x:
        m2["cnt"] += 1
    j += 1

    if k == len(m3["omr"]):
        k = 0
    if m3["omr"][k] == x:
        m3["cnt"] += 1
    k += 1

answer = []
maxx = max(m1["cnt"], m2["cnt"], m3["cnt"])
if maxx == m1["cnt"]:
    answer.append(1)
if maxx == m2["cnt"]:
    answer.append(2)
if maxx == m3["cnt"]:
    answer.append(3)
