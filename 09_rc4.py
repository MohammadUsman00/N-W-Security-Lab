# ============================================================
#  Lab 09 – RC4 Stream Cipher
# ============================================================
#
#  INPUT:
#    key       = "Secret"
#    plaintext = b"Hello RC4"
#
#  OUTPUT:
#    Plaintext : b'Hello RC4'
#    Encrypted : 4cb107695388291a75
#    Decrypted : b'Hello RC4'
#
# ============================================================

def rc4(key, data):
    # Key-Scheduling Algorithm (KSA)
    key = [ord(c) for c in key]
    S   = list(range(256))
    j   = 0
    for i in range(256):
        j    = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(result)

# --- Input ---
key       = "Secret"
plaintext = b"Hello RC4"

# --- Execution ---
encrypted = rc4(key, plaintext)
decrypted = rc4(key, encrypted)   # RC4 is symmetric – same operation decrypts

# --- Output ---
print(f"Plaintext : {plaintext}")           # Plaintext : b'Hello RC4'
print(f"Encrypted : {encrypted.hex()}")    # Encrypted : 4cb107695388291a75
print(f"Decrypted : {decrypted}")          # Decrypted : b'Hello RC4'
