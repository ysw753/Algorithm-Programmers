import math
w=12
h=12

plus=abs(w-h)
big=max(w,h)
answer=w*h-(w+h-math.gcd(w,h))
print(answer)