# ============================================================
#  Lab 06 – Extended Euclidean Algorithm
# ============================================================
#
#  INPUT:
#    a = 35
#    b = 15
#
#  OUTPUT:
#    GCD(35, 15) = 5
#    Coefficients: x = 1, y = -2
#    Verification: 35×1 + 15×-2 = 5
#
# ============================================================

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

# --- Input ---
a = 35
b = 15

# --- Execution ---
g, x, y = extended_gcd(a, b)

# --- Output ---
print(f"GCD({a}, {b}) = {g}")                               # GCD(35, 15) = 5
print(f"Coefficients: x = {x}, y = {y}")                   # Coefficients: x = 1, y = -2
print(f"Verification: {a}×{x} + {b}×{y} = {a*x + b*y}")   # Verification: 35×1 + 15×-2 = 5
