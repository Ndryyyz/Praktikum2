def main():
    print("Kalkulator Sederhana")
    #menmbaca input dari pengguna
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")
    #melakukan operasi berdasarkan input pengguna
    if operasi == '+':
        hasil = angka1 + angka2 
    elif operasi == '-':
        hasil = angka1 - angka2
    elif operasi == '*':
        hasil = angka1 * angka2
    elif operasi == '/':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
            
            return
        
    print(f"Hasil: {hasil}")

if __name__ == '__main__':1
main()