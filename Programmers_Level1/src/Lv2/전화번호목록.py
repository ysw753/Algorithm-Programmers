phone_book=["119", "97674223", "1195524421"]

answer=True
#11,1123,11324 이렇게 있으면 1123에서 걸려저서 11324볼필요가없다
phone_book.sort()


# 첫번째풀이 => 시간초과
# for i in range(len(phone_book)):
#   comlen=len(phone_book[i])
#   for j in range(i+1,len(phone_book)):
#     if phone_book[i]==phone_book[j][0:comlen]:
#       answer=False

# print(answer)

for i in range(len(phone_book)-1): 
  if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: 
    answer = False
    break


print(answer)
print(phone_book)
