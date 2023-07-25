total = 0
while True:
    jumlah = int(input("Masukkan jumlah barang : "))
    hrg = int(input("Masukkan harga satuan barangnya : "))
    harga = jumlah*hrg
    print(f"Total pembayaran = {harga}")
    total += harga
    
    while True:
        lanjut = input("Apakah ada lagi item yg dientrikan atau tidak? (y/n)")
        if lanjut == "y" :
            break
        elif lanjut == "n":
            kondisi = False
            break
        else:
            continue
    print(f"Total pembayaran = Rp{total}")