# ============================================================
#  Lab 10 – RSA (Rivest–Shamir–Adleman)
# ============================================================
#
#  INPUT:
#    p   = 61
#    q   = 53
#    msg = "HI"
#
#  OUTPUT:
#    p=61, q=53  →  n=3233
#    Public Key : e=65537, n=3233
#    Private Key: d=2753, n=3233
#    Plaintext  : HI
#    Encrypted  : [3000, 1486]
#    Decrypted  : HI
#
# ============================================================

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    return x % phi

def rsa_keygen(p, q):
    n   = p * q
    phi = (p - 1) * (q - 1)
    e   = 65537
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    return (e, n), (d, n)   # (public key, private key)

def rsa_encrypt(msg, pub_key):
    e, n = pub_key
    return [pow(ord(c), e, n) for c in msg]

def rsa_decrypt(cipher, priv_key):
    d, n = priv_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)

# --- Input ---
p   = 61
q   = 53
msg = "HI"

# --- Execution ---
pub, priv = rsa_keygen(p, q)
enc       = rsa_encrypt(msg, pub)
dec       = rsa_decrypt(enc, priv)

# --- Output ---
print(f"p={p}, q={q}  →  n={p*q}")              # p=61, q=53  →  n=3233
print(f"Public Key : e={pub[0]}, n={pub[1]}")    # Public Key : e=65537, n=3233
print(f"Private Key: d={priv[0]}, n={priv[1]}")  # Private Key: d=2753, n=3233
print(f"Plaintext  : {msg}")                      # Plaintext  : HI
print(f"Encrypted  : {enc}")                      # Encrypted  : [3000, 1486]
print(f"Decrypted  : {dec}")                      # Decrypted  : HI
