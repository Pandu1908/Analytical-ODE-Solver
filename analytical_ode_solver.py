import sympy as sp

# 1. Define symbolic variables and functions
t = sp.symbols('t')
y = sp.symbols('y', cls=sp.Function)

# 2. Define the differential equation: dy(t)/dt + 2*y(t) = 0
# Eq() represents the equality of left-hand side and right-hand side
ode = sp.Eq(y(t).diff(t), -2 * y(t))

# 3. Solve the equation analytically
# ics={y(0): 5} applies the initial condition y(0) = 5
analytical_solution = sp.dsolve(ode, ics={y(0): 5})

print("Exact analytical solution:")
print(analytical_solution)
