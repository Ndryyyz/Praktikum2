# Program sederhana untuk menemukan bilangan terbesar dari 4 bilangan menggunakan if statements

# Input 4 bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
bilangan4 = int(input("Masukkan bilangan keempat: "))

# Gunakan bilangan1 sebagai pembanding
# Bandingkan dengan bilangan2, bilangan3 dst..
if bilangan2 > bilangan1:
    bilangan1 = bilangan2

elif bilangan3 > bilangan1:
    bilangan1 = bilangan3
    
elif bilangan4 > bilangan1:
    bilangan1 = bilangan4


# Output bilangan terbesar
print(f"Bilangan terbesar adalah: {bilangan1}")

