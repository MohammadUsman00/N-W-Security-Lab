# ============================================================
#  Lab 02 – Playfair Cipher
# ============================================================
#
#  INPUT:
#    key  = "MONARCHY"
#    text = "INSTRUMENTS"
#
#  OUTPUT:
#    Key      : MONARCHY
#    Plaintext: INSTRUMENTS
#    Encrypted: GATLMZCLRQXA
#
# ============================================================

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen, matrix = set(), []
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_pos(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    pairs  = prepare_text(text)
    cipher = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

# --- Input ---
key  = "MONARCHY"
text = "INSTRUMENTS"

# --- Execution ---
enc = playfair_encrypt(text, key)

# --- Output ---
print(f"Key      : {key}")       # Key      : MONARCHY
print(f"Plaintext: {text}")      # Plaintext: INSTRUMENTS
print(f"Encrypted: {enc}")       # Encrypted: GATLMZCLRQXA
