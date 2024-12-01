from sympy import sec, Eq, symbols, solve

c = 329 % 10

x = symbols('x')

eq1 = Eq(2*x + 24*x, c + 1)
eq2 = Eq((c + 2)*x**3 - (c + 1)*x**2 - 5*x, -4*c)
eq3 = Eq((3 * sec((c - 3)*x) + 2)**2, 0)

sol1 = solve(eq1, x)

sol2 = solve(eq2, x)

sol3 = solve(eq3, x)

print(sol1)
print(sol2)
print(sol3)