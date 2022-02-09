from itertools import combinations

# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%9B%84%EB%B3%B4%ED%82%A4-Python 출처
# 어렵다

relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
]

row = len(relation)
col = len(relation[0])

combi = []

for i in range(1, col+1):
    combi.extend(combinations(range(col), i))

unique = []
for i in combi:
    tmp = [tuple([item[key] for key in i]) for item in relation]
    if len(set(tmp)) == row:
        put = True
        for x in unique:
            if set(x).issubset(set(i)):
                put = False
                break

        if put:
            unique.append(i)
print(len(unique))
