
numbers=[6, 10, 2]
numbers = list(map(str,numbers))

# 모두 3자리수 이상으로 만들어 비교함
# 666 1010 222 
#그러면 80 81 82 이런거 쉽게가능 8080 8181 8282

numbers.sort(key=lambda x:x*3 ,reverse=True)
answer=''.join(numbers)

if int(answer)==0:
  answer='0'
print(answer)