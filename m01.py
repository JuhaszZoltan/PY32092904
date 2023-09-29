kn:str = input('írj be egy keresztnevet: ')
vn:str = input('írj be egy vezetéknevet: ')
print(f'{vn} {kn}')
print(f'{kn} {vn}')
# ----------------------------------------
n:int = int(input('írj be egy számot: '))
print(f'előző szám: {n - 1}')
print(f'következő szám: {n + 1}')
# ----------------------------------------
x:int = int(input('írd be az első számot: '))
y:int = int(input('írd be a második számot: '))
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')
# ----------------------------------------
a:int = int(input('írd be az "a" értékét: '))
b:int = int(input('írd be az "b" értékét: '))
c:int = 2*a + 3*b
d:int = c - 2*a - 3*b
print(f'c értéke: {c}')
print(f'd értéke: {d}')
