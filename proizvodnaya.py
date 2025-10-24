import sympy

from sympy import solveset, Eq
from sympy import Symbol, S  # импортируем нужные функции для обозначения переменных
from sympy.calculus.util import function_range  # импортируем функцию для поиска области значений
from sympy import exp  # добавляем функцию для вычисления экспоненциальной функции
from sympy import diff, sin, exp, log, Symbol
from sympy import symbols, cos, diff, sin, solve, Eq


x = sympy.Symbol("x")
expr = x ** 2 + 9 * x - 5
print(expr.diff(x))

print('-' * 50)
print('Решить систему линейных уравнений')
x = symbols('x')
eq1 = Eq(-4*x**3 + 18*x**2 - 8*x, 0)
 
sol = solve([eq1], [x])
print(sol)