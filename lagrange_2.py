from sympy import *

x,y,w=symbols(' x y w ' )
g = x**2 + 2*y**2
print('Целевая функция для аргументов a и b :\n f = ', g)
print('-' * 50)

q = x + y - 20
print('Функция ограничений:\n ', q,'= 0')
print('-' * 50)

f = x**2 + 2*y**2 + w*(x + y - 20)
print('Функция Лагранжа :\n ',f)
print('-' * 50)

fx = f.diff(x)
print('df/da =',fx,'= 0')
fy = f.diff(y)
print('df/db =',fy,'= 0')
fw = f.diff(w)
print('df/dw =',fw,'= 0')
print('-' * 50)

sols = solve([fx,fy,fw],x,y,w)
print('Стационарная точка M(x,y):\n',float(sols[x]),',',float(sols[y]))