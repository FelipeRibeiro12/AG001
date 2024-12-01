import sympy as sp

c = 329 % 10

x = sp.symbols('x')

func = (1 + (c - 15)/sp.sqrt(x))**sp.sqrt(x)

lim1 = sp.limit(func, x, 0)

lim2 = sp.limit(func, x, sp.oo)

lim3 = sp.limit(func, x, -sp.oo)

print(lim1)
print(lim2)
print(lim3)