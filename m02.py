from math import pi

a:int = int(input('téglalap "a" oldala (cm): '))
b:int = int(input('téglalap "b" oldala (cm): '))
print(f'kerület: {2*(a+b)} cm')
print(f'terület: {a*b} cm^2')
#----------------------
r:int = int(input('kör sugara (cm): '))
print(f'kerület: {2*r*pi} cm')
print(f'terület: {r**2*pi} cm^2')
#---------------------
a:int = int(input('háromszög "a" oldala (cm): '))
b:int = int(input('háromszög "b" oldala (cm): '))
c:int = int(input('háromszög "c" oldala (cm): '))
k:int = a+b+c
print(f'kerület: {k} cm')
s:float = k/2
t:float = (s*(s-a)*(s-b)*(s-c))**.5
print(f'terület: {t} cm^2')