import sympy as sp

c = 329 % 10
A = 0.3  #amp
f = 9   #freq

omega = 2 * sp.pi * f

t = sp.symbols('t')

x_t = A * sp.sin(omega * t - c)

v_t = sp.diff(x_t, t)

a_t = sp.diff(v_t, t)

a_7 = a_t.subs(t, 7)

print(x_t)
print(a_t)
print(a_7)