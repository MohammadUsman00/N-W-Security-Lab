# ============================================================
#  Lab 11 – Diffie-Hellman Key Exchange
# ============================================================
#
#  INPUT:
#    p = 23   (prime modulus)
#    g = 5    (primitive root / generator)
#    a = 6    (Alice's private key)
#    b = 15   (Bob's private key)
#
#  OUTPUT:
#    Prime p = 23, Generator g = 5
#    Alice private = 6, Bob private = 15
#    Alice public  = 8, Bob public  = 19
#    Shared secret = 2  (both match: True)
#
# ============================================================

def diffie_hellman(p, g, a, b):
    A            = pow(g, a, p)   # Alice's public key
    B            = pow(g, b, p)   # Bob's public key
    alice_secret = pow(B, a, p)   # Alice computes shared secret
    bob_secret   = pow(A, b, p)   # Bob computes shared secret
    return A, B, alice_secret, bob_secret

# --- Input ---
p = 23    # prime
g = 5     # primitive root
a = 6     # Alice's private key
b = 15    # Bob's private key

# --- Execution ---
A, B, alice_s, bob_s = diffie_hellman(p, g, a, b)

# --- Output ---
print(f"Prime p = {p}, Generator g = {g}")              # Prime p = 23, Generator g = 5
print(f"Alice private = {a}, Bob private = {b}")        # Alice private = 6, Bob private = 15
print(f"Alice public  = {A}, Bob public  = {B}")        # Alice public  = 8, Bob public  = 19
print(f"Shared secret = {alice_s}  (both match: {alice_s == bob_s})")
                                                         # Shared secret = 2  (both match: True)
