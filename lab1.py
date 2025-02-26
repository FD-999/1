import math
k=(math.cos(5)/(4-math.sqrt(11)))+(math.sin(1)/(3+math.sqrt(7)))
p=2*(math.sin(5/13)+math.sin(12/13))*math.log(3)
if abs(k)<=2*abs(p):
    S=math.sqrt(3*k**2+4*p**2)
else:
    S=math.sqrt(3*p**2+4*5**2)
print(k)
print(p)
print(S)
