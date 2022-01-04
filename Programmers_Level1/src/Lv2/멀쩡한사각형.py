import math
w=12
h=12

answer=w*h-(w+h-math.gcd(w,h))
print(answer)