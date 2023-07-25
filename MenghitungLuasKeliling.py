print("===PROGRAM PENGHITUNG LUAS & KELILING===\n")

print("===Bangun yang tersedia===")
print("persegi [1]")
print("persegi panjang [2]")
print("segitiga [3]")
print("jajargenjang [4]")
print("trapesium [5]")
print("lingkaran [6]")
print("belah ketupat [7]")

bangun = int(input("\nPilih bangun sesuai nomer yg tersedia :"))
itung = input("Pilih ingin hitung luas [l] atau keliling [k] :")

if bangun == 1 :
    if itung == "l":
        sisi = int(input("Masukkan nilai sisi :"))
        luas = (sisi ** 2)
        print("Luas = ",luas, "cm^2")
    elif itung == "k":
        sisi = int(input("Masukkan nilai sisi :"))
        keliling = (sisi * 4)
        print("Keliling =", keliling, "cm")
if bangun == 2 :
    if itung == "l":
        sisi1 = int(input("Masukkan panjang :"))
        sisi2 = int(input("Masukkan lebar :"))
        luas = (sisi1 * sisi2)
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        sisi1 = int(input("Masukkan panjang :"))
        sisi2 = int(input("Masukkan lebar :"))
        keliling = (2 * (sisi1 + sisi2))
        print("Keliling =", keliling, "cm")
if bangun == 3 :
    if itung == "l":
        alas = int(input("Masukkan nilai alas :"))
        tinggi = int(input("Masukkan nilai tinggi :"))
        luas = ((alas * tinggi) / 2)
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        sisi1 = int(input("Masukkan nilai sisi 1 :"))
        sisi2 = int(input("Masukkan nilai sisi 2 :"))
        sisi3 = int(input("Masukkan nilai sisi 3 :"))
        keliling = (sisi1 + sisi2 + sisi3)
        print("Keliling =", keliling, "cm")
if bangun == 4 :
    if itung == "l" :
        alas = int(input("Masukkan nilai alas :"))
        tinggi = int(input("Masukkan nilai tinggi :"))
        luas = alas * tinggi
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        sisi1 = int(input("Masukkan nilai sisi 1 :"))
        sisi2 = int(input("Masukkan nilai sisi 2 :"))      
        keliling = (2 * (sisi1 + sisi2))
        print("Keliling =", keliling, "cm")
if bangun == 5 :
    if itung == "l" :
        atas = int(input("Masukkan nilai sisi atas :"))
        bawah = int(input("Masukkan nilai sisi bawah :"))
        tinggi = int(input("Masukkan nilai tinggi :"))
        luas = (((atas + bawah) * tinggi) / 2)
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        sisi1 = int(input("Masukkan nilai sisi 1 :"))
        sisi2 = int(input("Masukkan nilai sisi 2 :"))
        sisi3 = int(input("Masukkan nilai sisi 3 :"))
        sisi4 = int(input("Masukkan nilai sisi 4 :"))
        keliling = (sisi1 + sisi2 + sisi3 + sisi4)
        print("Keliling =", keliling, "cm")
if bangun == 6 :
    if itung == "l" :
        jari = int(input("Masukkan nilai jari-jari :"))
        phi = 22/7
        luas = (phi * (jari**2))
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        jari = int(input("Masukkan nilai jari-jari :"))
        phi = 22/7
        keliling = (phi *(jari * 2))
        print("Keliling =", keliling, "cm")
if bangun == 7 :
    if itung == "l" :
        diagonal1 = int(input("Masukkan nilai diagonal 1 :"))
        diagonal2 = int(input("Masukkan nilai diagonal 2 :"))
        luas = ((diagonal1 * diagonal2)/2)
        print("Luas = ",luas, "cm^2")
    elif itung == "k" :
        diagonal1 = int(input("Masukkan nilai diagonal 1 :"))
        diagonal2 = int(input("Masukkan nilai diagonal 2 :"))
        pitagoras = ((diagonal1)**(2) + (diagonal2)**(2))**(1/2)
        keliling = (4 * pitagoras)
        print("Keliling =", keliling, "cm")
        






























