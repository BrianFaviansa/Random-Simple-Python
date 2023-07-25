# program list buku 
import os
os.system("cls")
list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku = [judul,penulis]
    list_buku.append(buku)
    
    print("\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n","="*20)
    lanjut = input("Apakah dilanjutkan? (y/n) : ")
    if lanjut == "n":
        break
print("Program Selesai")























































