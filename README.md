# Network Security Lab Assignments

This repository contains the Python implementations for the Network Security Lab assignments.

**Student Information:**
* **Name:** Mohammad Numan Narwaroo
* **Roll No:** 220319
* **Semester:** 7th
* **Subject:** Network Security

## List of Programs

The following cryptographic algorithms and mathematical foundations are implemented in Python 3:

### Classical Ciphers
* `01_caesar_cipher.py` - Caesar Cipher Encryption & Decryption
* `02_playfair_cipher.py` - Playfair Cipher Encryption & Decryption
* `03_hill_cipher.py` - Hill Cipher Encryption & Decryption
* `04_rail_fence_cipher.py` - Rail Fence Cipher Encryption & Decryption

### Mathematical Foundations
* `05_euclidean_gcd.py` - Euclidean Algorithm (GCD)
* `06_extended_euclidean.py` - Extended Euclidean Algorithm
* `12_euler_totient.py` - Euler's Totient Function
* `13_crt.py` - Chinese Remainder Theorem (CRT)
* `14_fermat_theorem.py` - Fermat's Little Theorem & Primality Testing

### Modern Symmetric Ciphers
* `07_des.py` - Data Encryption Standard (DES)
* `08_aes.py` - Advanced Encryption Standard (AES)
* `09_rc4.py` - RC4 Stream Cipher

### Asymmetric Ciphers & Key Exchange
* `10_rsa.py` - RSA Algorithm (Key Generation, Encryption, Decryption)
* `11_diffie_hellman.py` - Diffie-Hellman Key Exchange

## Requirements and Execution

All scripts are written in pure Python 3. However, some scripts rely on external libraries for matrix operations and modern cryptographic primitives.

### Dependencies
Install the required dependencies using pip:
```bash
pip install numpy cryptography
```
* `numpy` is required for matrix multiplications in the Hill Cipher (`03_hill_cipher.py`).
* `cryptography` is required for DES (`07_des.py`) and AES (`08_aes.py`).

### Running the scripts
To execute any script, simply run it using python from the terminal. Each script contains the lab problem, test cases, and outputs comments.

Example:
```bash
python 01_caesar_cipher.py
```
