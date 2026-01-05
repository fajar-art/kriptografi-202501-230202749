import random

# Fungsi untuk membuat shares (Shamir Secret Sharing sederhana)
def split_secret(secret, n, k, prime=208351617316091241234326746312124448251235562226470491514186331217050270460481):
    shares = []
    coeffs = [secret] + [random.randrange(0, prime) for _ in range(k - 1)]

    for x in range(1, n + 1):
        y = 0
        for i, coeff in enumerate(coeffs):
            y += coeff * (x ** i)
        shares.append((x, y % prime))
    return shares

# Fungsi untuk rekonstruksi rahasia
def recover_secret(shares, prime):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num, den = 1, 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                num *= -xm
                den *= (xj - xm)
        secret += yj * num * pow(den, -1, prime)
    return secret % prime


# ================= MAIN PROGRAM =================

secret_text = "KriptografiUPB2025"
secret_int = int.from_bytes(secret_text.encode(), "big")

n = 5
k = 3
prime = 208351617316091241234326746312124448251235562226470491514186331217050270460481

shares = split_secret(secret_int, n, k, prime)
print("Shares:")
for s in shares:
    print(s)

recovered_int = recover_secret(shares[:3], prime)
recovered_text = recovered_int.to_bytes((recovered_int.bit_length() + 7) // 8, "big").decode()

print("\nRecovered secret:", recovered_text)
