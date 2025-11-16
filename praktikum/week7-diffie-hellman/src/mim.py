#simulasi man in the middle attack pada diffie-hellman
import random

# parameter umum (public)
p = 23
g = 5

# Private keys Alice dan Bob
a = random.randint(1, p-1)
b = random.randint(1, p-1)

# Eve juga memilih private key sendiri
e = random.randint(1, p-1)

# Public keys normal (tanpa serangan)
A_real = pow(g, a, p)  # Alice
B_real = pow(g, b, p)  # Bob

# Eve mencegat dan mengganti public key
A_fake_for_B = pow(g, e, p)  # Dikirim ke Bob seolah dari Alice
B_fake_for_A = pow(g, e, p)  # Dikirim ke Alice seolah dari Bob

# Alice menghitung shared key dgn key palsu dari Eve
shared_A_E = pow(B_fake_for_A, a, p)

# Bob menghitung shared key dgn key palsu dari Eve
shared_B_E = pow(A_fake_for_B, b, p)

# Eve menghitung kedua shared key
eve_with_A = pow(A_real, e, p)
eve_with_B = pow(B_real, e, p)

print("=== TANPA SERANGAN ===")
print("Public A:", A_real)
print("Public B:", B_real)
print()

print("=== DENGAN SERANGAN MITM OLEH EVE ===")
print("Kunci Alice-Eve :", shared_A_E)
print("Kunci Bob-Eve   :", shared_B_E)
print("Kunci Eve dengan Alice :", eve_with_A)
print("Kunci Eve dengan Bob   :", eve_with_B)
