# ============================================================
#  Lab 13 – Chinese Remainder Theorem (CRT)
# ============================================================
#
#  INPUT:
#    remainders = [2, 3, 2]
#    moduli     = [3, 5, 7]
#
#    Congruences:
#      x ≡ 2 (mod 3)
#      x ≡ 3 (mod 5)
#      x ≡ 2 (mod 7)
#
#  OUTPUT:
#    x ≡ 2 (mod 3)
#    x ≡ 3 (mod 5)
#    x ≡ 2 (mod 7)
#    Solution: x = 23
#
# ============================================================

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def crt(remainders, moduli):
    M  = 1
    for m in moduli:
        M *= m            # Product of all moduli
    x = 0
    for r, m in zip(remainders, moduli):
        Mi       = M // m
        _, inv, _ = extended_gcd(Mi, m)
        x        += r * Mi * inv
    return x % M

# --- Input ---
remainders = [2, 3, 2]
moduli     = [3, 5, 7]

# --- Execution ---
result = crt(remainders, moduli)

# --- Output ---
print(f"x ≡ {remainders[0]} (mod {moduli[0]})")   # x ≡ 2 (mod 3)
print(f"x ≡ {remainders[1]} (mod {moduli[1]})")   # x ≡ 3 (mod 5)
print(f"x ≡ {remainders[2]} (mod {moduli[2]})")   # x ≡ 2 (mod 7)
print(f"Solution: x = {result}")                   # Solution: x = 23
