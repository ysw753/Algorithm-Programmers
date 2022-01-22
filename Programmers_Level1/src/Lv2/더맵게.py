import heapq
scoville = [1, 2, 3, 9, 10, 12]
k = 7
answer = 0

# #시간초과
# while min(scoville) < k:
#     if len(scoville) == 1:
#         answer = -1
#         break
#     scoville.sort()
#     minn1 = scoville.pop(0)
#     minn2 = scoville.pop(0)
#     scoville.append(minn1+(minn2*2))
#     answer += 1
# print(answer)

# heapq를 쓴코드
heap = []
for x in scoville:
    heapq.heappush(heap, x)
while heap[0] < k:
    if len(heap) == 1:
        answer = -1
        break
    heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
    answer += 1
print(answer)
