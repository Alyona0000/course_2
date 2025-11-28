import sympy as sp
from sympy import sin, cos, exp, ln, sqrt, Function, integrate, diff, limit, summation, product, series
import numpy as np
import matplotlib.pyplot as plt


# Змінні
x, y, t, n, k = sp.symbols('x y t n k', real=True)
a = sp.symbols('a', real=True, positive=True)
f = Function('f')
g = Function('g')

print("\n1. Для функції f(x) = (sin^2(x) cos(x) + t^3) / t підставити t = cos(x) і спростити вираз.\n")
fx = (sp.sin(x)**2 * sp.cos(x) + t**3) / t
fx_sub = sp.simplify(fx.subs(t, sp.cos(x)))
print("Результат:", fx_sub)

print("\n2. Обчислити і спростити вирази:\n")
expr2a = sp.simplify((x**3 - x**2 + x - 1) / (x**2 - 1))
expr2b = sp.simplify(((x**2 + 2*x + 1)**2 - (x**2 - 1)**2) / (x + 1))
expr2c = sp.simplify((ln(x**2) - 2*ln(x)) / ln(x))   # за текстом твого завдання
print("a) (x^3 − x^2 + x − 1) / (x^2 − 1) =", expr2a)
print("b) ((x^2 + 2x + 1)^2 − (x^2 − 1)^2) / (x + 1) =", expr2b)
print("c) (ln(x^2) − 2 ln(x)) / ln(x) =", expr2c)

print("\n3. Розкласти на прості множники вирази:\n")
expr3a = sp.factor(x**4 - 2*x**2*y**2 + y**4)
expr3b = sp.factor(x**4 - 5*x**2 + 4)
expr3c = sp.factor(x**5 - x)
expr3d = sp.factor(x**8 - y**8)
print("a) x^4 − 2x^2 y^2 + y^4 =", expr3a)
print("b) x^4 − 5x^2 + 4 =", expr3b)
print("c) x^5 − x =", expr3c)
print("d) x^8 − y^8 =", expr3d)

print("\n4. Згрупувати подібні члени за змінною x:\n")
expr4a = x**3 + 2*x*y**2 + 5*x**2 - 3*x*y + 7*x + 4*y*x + 5*y + 6
expr4b = x**6*y**6 + 3*x**3 + y*x**3 + 5*x**2 - 3*x*y
print("a) x^3 + 2xy^2 + 5x^2 − 3xy + 7x + 4yx + 5y + 6 =", sp.simplify(expr4a))
print("b) x^6 y^6 + 3x^3 + yx^3 + 5x^2 − 3xy =", sp.simplify(expr4b))

print("\n5. Знайти значення границь:\n")
lim5a = limit((sin(3*x) - 3*x) / x**3, x, 0)
lim5b = limit((exp(2*x) - 1 - 2*x) / x**2, x, 0)
lim5c = limit(x*(sqrt(x**2 + 1) - x), x, sp.oo)
lim5d = limit((x**x - 1) / (x - 1), x, 1)
print("a) lim_{x→0} (sin(3x) − 3x) / x^3 =", lim5a)
print("b) lim_{x→0} (e^{2x} − 1 − 2x) / x^2 =", lim5b)
print("c) lim_{x→∞} x(√(x^2 + 1) − x) =", lim5c)
print("d) lim_{x→1} (x^x − 1) / (x − 1) =", lim5d)

print("\n6. Обчислити відповідні суми та добутки:\n")
sum6a = summation(k**2, (k, 1, n))
sum6b = summation((sp.Rational(1, 2))**k, (k, 0, sp.oo))
sum6c = summation(1/k**2, (k, 1, sp.oo))
sum6d = summation((-1)**(k+1)/k, (k, 1, sp.oo))
prod6e = product(k, (k, 1, n))
# нескінченний добуток замінимо на наближення
prod6f_approx = product(1 - x**2/k**2, (k, 1, 10))
print("a) ∑_{k=1}^n k^2 =", sum6a)
print("b) ∑_{k=0}^∞ (1/2)^k =", sum6b)
print("c) ∑_{k=1}^∞ 1/k^2 =", sum6c)
print("d) ∑_{k=1}^∞ (-1)^{k+1} / k =", sum6d)
print("e) ∏_{k=1}^n k =", prod6e)
print("f) ∏_{k=1}^∞ (1 − x^2/k^2) ≈ (добуток до 10):", sp.simplify(prod6f_approx))

print("\n7. Знайти першу, другу та третю похідні для функцій:\n")

def show_derivs(expr, label):
    print(label)
    print("  f(x) =", expr)
    print("  f'(x)  =", diff(expr, x))
    print("  f''(x) =", diff(expr, x, 2))
    print("  f'''(x)=", diff(expr, x, 3))
    print()

show_derivs(sin(x)*cos(x**2), "a) f(x) = sin(x) cos(x^2)")
show_derivs(exp(x**2)*sin(x), "b) f(x) = e^{x^2} sin(x)")
show_derivs(ln(x**2 + 1) / x, "c) f(x) = ln(x^2 + 1) / x, x ≠ 0")
show_derivs(exp(sin(x)) + x**2*ln(x + 1), "d) f(x) = e^{sin(x)} + x^2 ln(x + 1)")
show_derivs((x**2 + 1)*sin(x), "e) f(x) = (x^2 + 1) sin(x)")

print("\n8. Обчислити інтеграли:\n")
I8a = integrate(x**2 * exp(x), x)
I8b = integrate(x**3 * sp.log(x), (x, 0, 1))               # за змістом — від 0 до 1
I8c = integrate(x**a * exp(-x), (x, 0, sp.oo))             # параметр a
I8d = integrate(sin(x)**3, (x, 0, sp.pi/2))
I8e = integrate(exp(-a*x**2), (x, 0, sp.oo))
I8f = integrate(sp.tan(x), (x, 0, sp.pi/4))
z = sp.symbols('z', real=True)
I8g = integrate(x*y*z, (z, 0, 1), (y, 0, 1), (x, 0, 1))
I8h = integrate(1/(1 + x**4), (x, -sp.oo, sp.oo))
I8i = integrate(exp(-x)*sin(x), (x, 0, sp.oo))
I8j = integrate(x + y**2, (x, 0, 1 - y), (y, 0, 1))

print("a) ∫ x^2 e^x dx =", I8a)
print("b) ∫_0^1 x^3 log(x) dx =", I8b)
print("c) ∫_0^∞ x^a e^{-x} dx =", I8c)
print("d) ∫_0^{π/2} sin^3(x) dx =", I8d)
print("e) ∫_0^∞ e^{-a x^2} dx =", I8e)
print("f) ∫_0^{π/4} tan(x) dx =", I8f)
print("g) ∭_{[0,1]^3} x y z dV =", I8g)
print("h) ∫_{-∞}^{∞} 1/(1 + x^4) dx =", I8h)
print("i) ∫_0^∞ e^{-x} sin(x) dx =", I8i)
print("j) ∫_0^1 ∫_0^{1 − y} (x + y^2) dx dy =", I8j)

print("\n9. Знайти розклади в ряд Тейлора в околі точки 0:\n")
series9a = series(exp(x), x, 0, 7)      # 7 доданків
series9b = series(sin(x), x, 0, 7)      # 3 ненульових доданки, але берем до x^7
series9c = series(1/(1 - x), x, 0, 6)
series9d = series(exp(sin(x)), x, 0, 6)
series9e = series(ln(1 + x), x, 0, 6)

print("a) e^x (7 доданків):", series9a)
print("b) sin(x) (перші 3 ненульові доданки):", series9b)
print("c) 1/(1 − x):", series9c)
print("d) e^{sin(x)}:", series9d)
print("e) ln(1 + x):", series9e)

print("\n10. Знайти загальний розв’язок диференціальних рівнянь:\n")
# 10a: f'(x) = −5 f(x)
ode10a = sp.Eq(diff(f(x), x), -5*f(x))
sol10a = sp.dsolve(ode10a)
print("a) f'(x) = −5 f(x) →", sol10a)

# 10b: в тексті каша, беремо як f''(x) = −cos(x)/2 (просто осмислений варіант)
ode10b = sp.Eq(diff(f(x), x, 2), -sp.cos(x)/2)
sol10b = sp.dsolve(ode10b)
print("b) f''(x) = −(1/2) cos(x) →", sol10b)

# 10c: f''(x) + 3 (f'(x))^2 = 0 — SymPy, швидше за все, не вирішить
ode10c = sp.Eq(diff(f(x), x, 2) + 3*diff(f(x), x)**2, 0)
print("c) f''(x) + 3(f'(x))^2 = 0 → аналітичний розв’язок SymPy знайти важко, пропускаємо.")

print("\n11. Знайти загальний розв’язок задачі Коші та побудувати його графік (аналітично розв’язуємо):\n")
# f'(x) = −5 f(x) + x^2, f(0) = 1
ode11 = sp.Eq(diff(f(x), x), -5*f(x) + x**2)
sol11 = sp.dsolve(ode11, ics={f(0): 1})
print("f'(x) = −5 f(x) + x^2, f(0) = 1 →", sol11)

print("\n12. Знайти розв’язок однорідних та неоднорідних диференціальних рівнянь із сталими коефіцієнтами:\n")
eq12a = sp.Eq(2*diff(f(x), x, 2) - 4*diff(f(x), x) + 2*f(x), 0)
eq12b = sp.Eq(diff(f(x), x, 4) + 2*diff(f(x), x, 3) - 2*diff(f(x), x, 2) - 6*diff(f(x), x) + 5*f(x), 0)
sol12a = sp.dsolve(eq12a)
sol12b = sp.dsolve(eq12b)
print("a) 2 f''(x) − 4 f'(x) + 2 f(x) = 0 →", sol12a)
print("b) f⁽⁴⁾(x) + 2 f⁽³⁾(x) − 2 f''(x) − 6 f'(x) + 5 f(x) = 0 →", sol12b)

print("\n13. Нехай маємо наступну систему ЗДР:\n"
      "   f'(t) = g(t)\n"
      "   g'(t) = −2 f(t)\n")


# ---- система ----
t = sp.symbols('t', real=True)
F = sp.Function('F')
G = sp.Function('G')

# Розв'язок задачі Коші
sol = sp.dsolve([
        sp.Eq(sp.diff(F(t), t), G(t)),
        sp.Eq(sp.diff(G(t), t), -2*F(t))
    ],
    ics={F(0): 1, G(0): 0}
)

F_sol = sp.lambdify(t, sol[0].rhs, 'numpy')
G_sol = sp.lambdify(t, sol[1].rhs, 'numpy')

# ---- сітка для графіка ----
t_vals = np.linspace(0, 10, 400)

# ---- побудова ----
plt.figure(figsize=(10,5))
plt.plot(t_vals, F_sol(t_vals), label='F(t)', linewidth=2)
plt.plot(t_vals, G_sol(t_vals), label='G(t)', linewidth=2)

plt.title("Розв’язок задачі Коші системи F'(t)=G(t), G'(t)=-2F(t)")
plt.xlabel("t")
plt.ylabel("значення функцій")
plt.grid(True)
plt.legend()
plt.show()








