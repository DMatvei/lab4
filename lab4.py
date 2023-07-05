import math
from scipy import integrate
 

def newton_cotes_formula(h, a, b):
    c = [1/6, 4/6, 1/6]
 
    arr_x = [a + i * h for i in range(m+1)]
    arr_y = [x**2 - math.sin(x) for x in arr_x]
    I = 0
 
    for k in range(m+1):
      I += c[k] * arr_y[k]
    I *= (b - a)
 
    return I
 
 
def f(x):
    return (x**2 - math.sin(x))
 
a = 0.5
b = 1.0
n = 2
m = 2
eps = 0.00000001
 
 
I1 = newton_cotes_formula((b-a)/n, a, b)
 
mid = (a + b) / 2 
parts = 2 
n *= 2 
I2 = newton_cotes_formula((mid-a)/m, a, mid) 
I2 += newton_cotes_formula((b-mid)/m, mid, b) 
 
while (abs(I1 - I2) > eps): 
    I1 = I2 
    I2 = 0 
    parts *= 2 
    n *= 2
    h = (b - a) / n 
    for i in range(1, parts+1): 
      left = a + (i - 1) * 2 * h 
      right = a + i * 2 * h 
      I2 += newton_cotes_formula(h, left, right) 
 
print(f'{I2} - интеграл, вычисленный с точностью eps = {eps}')
 
result, error = integrate.quad(f, a, b)
print(f'{result} - интеграл, посчитанный с помощью встроенной функции')