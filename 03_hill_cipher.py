# ============================================================
#  Lab 03 – Hill Cipher
# ============================================================
#
#  INPUT:
#    text       = "ACT"
#    key_matrix = [[6, 24, 1],
#                  [13, 16, 10],
#                  [20, 17, 15]]
#
#  OUTPUT:
#    Plaintext: ACT
#    Key Matrix:
#    [[ 6 24  1]
#     [13 16 10]
#     [20 17 15]]
#    Encrypted: POH
#
#  Requires: pip install numpy
# ============================================================

import numpy as np

def hill_encrypt(text, key_matrix):
    text = text.upper()
    n    = len(key_matrix)
    while len(text) % n != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), n):
        block = [ord(c) - ord('A') for c in text[i:i+n]]
        enc   = np.dot(key_matrix, block) % 26
        result += ''.join(chr(int(v) + ord('A')) for v in enc)
    return result

# --- Input ---
key_matrix = np.array([[6, 24, 1],
                        [13, 16, 10],
                        [20, 17, 15]])
text = "ACT"

# --- Execution ---
enc = hill_encrypt(text, key_matrix)

# --- Output ---
print(f"Plaintext: {text}")              # Plaintext: ACT
print(f"Key Matrix:\n{key_matrix}")      # Key Matrix:
                                          # [[ 6 24  1]
                                          #  [13 16 10]
                                          #  [20 17 15]]
print(f"Encrypted: {enc}")               # Encrypted: POH
