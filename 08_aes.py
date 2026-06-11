# ============================================================
#  Lab 08 – AES (Advanced Encryption Standard)
# ============================================================
#
#  INPUT:
#    key  = b'mysecretkey12345'   (16 bytes → AES-128)
#    text = "HELLO WORLD"
#
#  OUTPUT:
#    Plaintext : HELLO WORLD
#    Encrypted : 88aa135c8366a6aaa7ec60b06c8918f7
#    Decrypted : HELLO WORLD
#
#  Requires: pip install cryptography
# ============================================================

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def aes_encrypt(plaintext, key):
    # Pad / truncate plaintext to exactly 16 bytes
    plaintext = plaintext.encode().ljust(16, b'\x00')[:16]
    cipher    = Cipher(algorithms.AES(key), modes.ECB(),
                       backend=default_backend())
    return cipher.encryptor().update(plaintext)

def aes_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(),
                    backend=default_backend())
    return cipher.decryptor().update(ciphertext).rstrip(b'\x00').decode()

# --- Input ---
key  = b'mysecretkey12345'   # 16 bytes for AES-128
text = "HELLO WORLD"

# --- Execution ---
enc = aes_encrypt(text, key)
dec = aes_decrypt(enc, key)

# --- Output ---
print(f"Plaintext : {text}")          # Plaintext : HELLO WORLD
print(f"Encrypted : {enc.hex()}")    # Encrypted : 88aa135c8366a6aaa7ec60b06c8918f7
print(f"Decrypted : {dec}")          # Decrypted : HELLO WORLD
