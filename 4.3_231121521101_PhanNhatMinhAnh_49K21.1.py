# RSA encrypt per character (ASCII)
p, q, e = 17, 23, 5
n = p * q            # 391
phi = (p-1) * (q-1)  # 352

plaintext = "PhanNhatMinhAnh"

# Encrypt: c = m^e mod n for each ASCII code m
cipher = [pow(ord(ch), e, n) for ch in plaintext]
print("n =", n, "phi(n) =", phi)
print("Plain ASCII:", [ord(ch) for ch in plaintext])
print("Cipher ints:", cipher)

# (Optional) Decrypt for check:
# d is modular inverse of e mod phi(n) -> 5 * 141 ≡ 1 (mod 352) => d = 141
d = 141
recovered = "".join(chr(pow(c, d, n)) for c in cipher)
print("Recovered:", recovered)
