
from typing import Deque


new_id ="...!@BaT#*..y.abcdefghijklm"

new_id=new_id.lower()
new_id=Deque(new_id)
answer=''

while new_id:
  tmp=new_id.popleft()
  if tmp.isdecimal() or tmp.isalpha():
    answer+=tmp
  elif tmp=='-' or tmp=='_' or tmp=='.':
    answer+=tmp
while True:
  if '..' in answer:
    answer=answer.replace('..','.')
  if '..' not in answer:
    break
if answer==''or answer=='.':
  answer+='a'
  
if answer[0]=='.':
  answer=answer[1:]
if answer[-1]=='.':
  answer=answer[:-1]


if len(answer)>=16:
  answer=answer[0:15]
  if answer[-1] == '.':
    answer = answer[:-1]
if len(answer)<=3:
  answer+=answer[-1]*(3-len(answer))
  

print(answer)