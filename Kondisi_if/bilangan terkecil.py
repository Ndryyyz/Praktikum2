# Program sederhana untuk menemukan bilangan terbesar dari 4 bilangan menggunakan if statements

# Input 4 bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
bilangan4 = int(input("Masukkan bilangan keempat: "))

# Sorting manual
if bilangan1 > bilangan2:
    bilangan1, bilangan2 = bilangan2, bilangan1
if bilangan2 > bilangan3:
    bilangan2, bilangan3 = bilangan3, bilangan2
if bilangan3 > bilangan4:
    bilangan3, bilangan4 = bilangan4, bilangan3

if bilangan1 > bilangan2:
    bilangan1, bilangan2 = bilangan2, bilangan1
if bilangan2 > bilangan3:
    bilangan2, bilangan3 = bilangan3, bilangan2

if bilangan1 > bilangan2:
    bilangan1, bilangan2 = bilangan2, bilangan1
# Output bilangan terkecil ke terbesar
print("urutan bilangan:", bilangan1, bilangan2, bilangan3, bilangan4)

