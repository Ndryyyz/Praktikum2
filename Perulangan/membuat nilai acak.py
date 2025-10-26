n = int(input("Berapa angka random yang mau ditampilkan? "))

for i in range(n):
    seed = i * 789
    j = 0
    
    while j < 1:  # Loop sampai dapat angka < 0.5
        seed = (seed * 1103515245 + 12345) % 2147483648
        angka = seed / 2147483648
        if angka < 0.5:
            print(f"{angka:.10f}")
            j += 1