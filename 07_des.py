# ============================================================
#  Lab 07 – DES (Data Encryption Standard)
# ============================================================
#
#  INPUT:
#    key  = b'secret!!'   (8 bytes)
#    text = "HELLO"
#
#  OUTPUT:
#    Plaintext : HELLO
#    Encrypted : 92f48ab57d00f0bd
#    Decrypted : HELLO
#
#  Requires: pip install cryptography
# ============================================================

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def des_encrypt(plaintext, key):
    # Pad / truncate plaintext to exactly 8 bytes
    plaintext = plaintext.encode().ljust(8, b'\x00')[:8]
    # TripleDES with the same 8-byte key repeated ×3 = 24 bytes
    cipher    = Cipher(algorithms.TripleDES(key * 3), modes.ECB(),
                       backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()

def des_decrypt(ciphertext, key):
    cipher    = Cipher(algorithms.TripleDES(key * 3), modes.ECB(),
                       backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).rstrip(b'\x00')

# --- Input ---
key  = b'secret!!'   # 8 bytes
text = "HELLO"

# --- Execution ---
enc = des_encrypt(text, key)
dec = des_decrypt(enc, key)

# --- Output ---
print(f"Plaintext : {text}")          # Plaintext : HELLO
print(f"Encrypted : {enc.hex()}")    # Encrypted : 92f48ab57d00f0bd
print(f"Decrypted : {dec.decode()}") # Decrypted : HELLO
