from sympy import symbols, cos, diff, sin, solve, Eq
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import least_squares


a, b, x = symbols('a b x', real=True)
expr = 2*a*x + b**2

print(diff(expr, a))


x, y = symbols('x y', real=True)
expr = y * sin(x) + sin(y)

print(diff(expr, y))

def func_rosen(x):
    r = np.sum(100*(x[1:]-x[:-1]**2)**2 + (1-x[:-1])**2, axis=0)
    return r

def func_my(x):
    return np.mean(x)
x1 = np.array([2.4, 1.5, 2.1, 2100, 1.1])
# x1 = np.array([1, 1])
#  метод Пауэлла
result_point = minimize(func_rosen, x1, method='powell')
print(result_point.x)


# print(func_my(x1))
# print('+++++++')
# result = least_squares(func_my, x1)
# print(result.x)
print('-' * 50)
print('Нахождение производной')
x, y, z = symbols('x y z', real=True)

expr = 8*x**3 - 2*x**2-450

print("Исходное выражение:", expr)
print()

# Первые производные
f_x = diff(expr, x)
f_y = diff(expr, y)
f_z = diff(expr, z)
print("Первые производные:")
print("∂f/∂x =", f_x)
print("∂f/∂y =", f_y)
print("∂f/∂z =", f_z)
print()

# Вторые производные
print("Вторые производные:")
# Чистые вторые производные
f_xx = diff(expr, x, x)  # или diff(f_x, x)
f_yy = diff(expr, y, y)  # или diff(f_y, y)

# Смешанные производные
f_xy = diff(expr, x, y)  # или diff(f_x, y)
f_yx = diff(expr, y, x)  # или diff(f_y, x)

print("∂²f/∂x² =", f_xx)
print("∂²f/∂y² =", f_yy)
print("∂²f/∂x∂y =", f_xy)
print("∂²f/∂y∂x =", f_yx)   




print('-' * 50)
print('Нахождение собственных чисел')
A = np.array([[6, -3],
              [-3, 6]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# print("Матрица A:")
# print(A)
print("\nСобственные значения:")
print(eigenvalues)
print("\nСобственные векторы (столбцы):")
print(eigenvectors)

print('-' * 50)
print('Решить систему линейных уравнений')
x, y, z = symbols('x, y, z')
eq1 = Eq(2*x*z + 4, 0)
eq2 = Eq(2*y*z + 3, 0)
eq3 = Eq(x**2 + y**2 - 1, 0)
 
sol = solve([eq1, eq2, eq3], [x, y, z])
print(sol)