from sympy import symbols, Eq, solve

c = 329 % 10

i1, i2, i3 = symbols('i1 i2 i3')

V1 = 3 + (4 * c)
V2 = -1 - (5 * c)

eq1 = Eq(i1 * 2 + (i1 - i2) * 4 + (i1 - i3) * 6, V1)

eq2 = Eq((i2 - i1) * 4 + i2 * 3 + (i2 - i3) * 2, V2)

eq3 = Eq((i3 - i1) * 6 + (i3 - i2) * 2 + i3 * 5, 0)

correntes = solve([eq1, eq2, eq3], [i1, i2, i3])

print(correntes)