import sympy as sp

c = 329 % 10

t = sp.symbols('t')

S = ((-2*t**4)/3) + (5*sp.sqrt(t)) - c

v = sp.diff(S, t)

v_t8 = v.subs(t, 8)

a = sp.diff(v, t)

a_t9 = a.subs(t, 9)

print(v)
print(v_t8)
print(a)
print(a_t9)