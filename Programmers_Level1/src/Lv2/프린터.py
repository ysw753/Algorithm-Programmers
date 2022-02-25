from collections import deque


priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 0
d = deque([(v, i) for i, v in enumerate(priorities)])
while len(d):
    item = d.popleft()
    if d and max(d)[0] > item[0]:
        d.append(item)
    else:
        answer += 1
        if item[1] == location:
            break
print(answer)

# 배열두개로푸는법(인데스 저장해서)
# idx = [c for c in range(len(priorities))]
# arr = priorities.copy()
# i = 0

# while True:
#     if arr[i] < max(arr[i+1:]):
#         idx.append(idx.pop(i))
#         arr.append(arr.pop(i))
#     else:
#         i += 1

#     if arr == sorted(arr, reverse=True):
#         break

# print(idx.index(location)+1)


# def solution(priorities, location):
#     answer = 0
#     search, c = sorted(priorities, reverse=True), 0
#     while True:
#         for i, priority in enumerate(priorities):
#             s = search[c]
#             if priority == s:
#                 c += 1
#                 answer += 1
#                 if i == location:
#                     break
#         else:
#             continue
#         break
#     return answer
