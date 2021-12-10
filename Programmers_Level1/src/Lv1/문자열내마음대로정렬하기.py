strings=["sun", "bed", "car"]
n=1

standard=[]
for x in strings:
  standard.append(x[n]+x)
  standard.sort()
answer=[i[1:] for i in standard]

print(answer)



# #키로 정렬하는법 단 이경우  abce abcd 면 그대로 출력됨
# strings=sorted(strings,key=lambda x:x[n])
# print(strings)