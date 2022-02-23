citations = [0, 0, 0, 0, 0]

# 나의풀이
cnt1 = 0
cnt2 = 0
res = 0
minn = 0

for i in range(0, max(citations)):
    for citation in citations:
        if citation >= i:
            cnt1 += 1
        if citation <= i:
            cnt2 += 1
    if cnt1 >= i and cnt2 <= i:
        res = i
    if minn < res:
        minn = res
    cnt1 = 0
    cnt2 = 0
print(minn)


# 인터넷 풀이
def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0


answer = solution(citations)
print(answer)

# 고수의 풀이


def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


answer2 = solution2(citations)
print(answer2)
