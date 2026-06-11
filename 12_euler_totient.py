# ============================================================
#  Lab 12 – Euler's Totient Function
# ============================================================
#
#  INPUT:
#    n values: 9, 10, 36
#
#  OUTPUT:
#    φ(9)  = 6
#    φ(10) = 4
#    φ(36) = 12
#
# ============================================================

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    # Count integers from 1..n that are coprime with n
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

# --- Input / Output ---
for n in [9, 10, 36]:
    print(f"φ({n}) = {euler_totient(n)}")
    # φ(9)  = 6
    # φ(10) = 4
    # φ(36) = 12
