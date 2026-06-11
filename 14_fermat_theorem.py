# ============================================================
#  Lab 14 – Fermat's Theorem (Little Theorem + Primality Test)
# ============================================================
#
#  INPUT:
#    Fermat demo: (a=3, p=7) and (a=2, p=13)
#    Primality test: n in [7, 11, 15, 23, 25]
#
#  OUTPUT:
#    === Fermat's Little Theorem ===
#    3^(7-1) mod 7 = 1  →  Confirmed
#    2^(13-1) mod 13 = 1  →  Confirmed
#
#    === Primality Testing ===
#    7 is probably prime
#    11 is probably prime
#    15 is composite
#    23 is probably prime
#    25 is composite
#
# ============================================================

import random

def fermat_primality_test(n, k=5):
    """Returns True if n is probably prime (False if definitely composite)."""
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def fermat_little_theorem_demo(a, p):
    """Demonstrate Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p) when p is prime."""
    result = pow(a, p - 1, p)
    label  = 'Confirmed' if result == 1 else 'Not prime'
    print(f"{a}^({p}-1) mod {p} = {result}  →  {label}")

# --- Fermat's Little Theorem ---
print("=== Fermat's Little Theorem ===")
fermat_little_theorem_demo(3, 7)    # 3^(7-1) mod 7 = 1  →  Confirmed
fermat_little_theorem_demo(2, 13)   # 2^(13-1) mod 13 = 1  →  Confirmed

# --- Primality Testing ---
print("\n=== Primality Testing ===")
for n in [7, 11, 15, 23, 25]:
    label = 'probably prime' if fermat_primality_test(n) else 'composite'
    print(f"{n} is {label}")
    # 7  is probably prime
    # 11 is probably prime
    # 15 is composite
    # 23 is probably prime
    # 25 is composite
