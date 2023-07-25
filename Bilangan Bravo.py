a = int(input("Masukkan angka 1 : "))
b = int(input("Masukkan angka 2 : "))
c = int(input("Masukkan angka 3 : "))
d = int(input("Masukkan angka 4 : "))
angka = (f"{a}{b}{c}{d}")
print(f"angka anda adalah = {angka}")
e = a+b+c+d
f = e%a and e%b and e%c and e%d

if f == 0:
    hasil = f"{angka} merupakan bilangan bravo"
else:
    hasil = f"{angka} bukan merupakan bilangan bravo"
    
print(hasil)








