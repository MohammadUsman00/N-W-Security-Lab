# ============================================================
#  Lab 01 – Caesar Cipher
# ============================================================
#
#  INPUT:
#    text  = "HELLO"
#    shift = 3
#
#  OUTPUT:
#    Original : HELLO
#    Encrypted: KHOOR
#    Decrypted: HELLO
#
# ============================================================

def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- Input ---
text  = "HELLO"
shift = 3

# --- Execution ---
enc = caesar_encrypt(text, shift)
dec = caesar_decrypt(enc, shift)

# --- Output ---
print(f"Original : {text}")      # Original : HELLO
print(f"Encrypted: {enc}")       # Encrypted: KHOOR
print(f"Decrypted: {dec}")       # Decrypted: HELLO
