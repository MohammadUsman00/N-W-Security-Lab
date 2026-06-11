# ============================================================
#  Lab 04 – Rail Fence Cipher
# ============================================================
#
#  INPUT:
#    text  = "WEAREDISCOVEREDFLEEAYNOW"
#    rails = 3
#
#  OUTPUT:
#    Original : WEAREDISCOVEREDFLEEAYNOW
#    Encrypted: WECRLYERDSOEEFEANWAIVDEO
#    Decrypted: WEAREDISCOVEREDFLEEAYNOW
#
# ============================================================

def rail_fence_encrypt(text, rails):
    fence     = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in text:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in fence)

def rail_fence_decrypt(cipher, rails):
    n    = len(cipher)
    rail, direction = 0, 1
    pattern = []
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    idx    = 0
    counts = [pattern.count(r) for r in range(rails)]
    chunks = []
    for count in counts:
        chunks.append(list(cipher[idx:idx+count]))
        idx += count
    result   = ""
    pointers = [0] * rails
    for r in pattern:
        result += chunks[r][pointers[r]]
        pointers[r] += 1
    return result

# --- Input ---
text  = "WEAREDISCOVEREDFLEEAYNOW"
rails = 3

# --- Execution ---
enc = rail_fence_encrypt(text, rails)
dec = rail_fence_decrypt(enc, rails)

# --- Output ---
print(f"Original : {text}")   # Original : WEAREDISCOVEREDFLEEAYNOW
print(f"Encrypted: {enc}")    # Encrypted: WECRLYERDSOEEFEANWAIVDEO
print(f"Decrypted: {dec}")    # Decrypted: WEAREDISCOVEREDFLEEAYNOW
