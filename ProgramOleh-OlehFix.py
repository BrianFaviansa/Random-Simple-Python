barang = []
harga = []

print ("----------------------Toko Oleh-oleh Khas Jember------------------------")
list = {"suwar-suwir" : "17000" ,
     "prol tape" : "20000" ,
     "dodol tape": "15000" ,
     "tape besek" : "18000" ,
     "bakpia tape" : "13000" ,
     "tape bakar" : "15000" ,
     "madu mongso" : "12000"
}
list_makanan = {"produk makanan" : list}
print (list_makanan)
print ("""Daftar Produk Makanan dan Harga
    a. suwar-suwir : Rp 17.000
    b. prol tape   : Rp 20.000
    c. dodol tape  : Rp 15.000
    d. tape besek  : Rp 18.000
    e. bakpia tape : Rp 13.000
    """) 

beli = str(input("masukkan list abjad makanan = "))
produk = ("suwar-suwir", "prol tape", "dodol tape", "tape besek", "bakpia tape")
jumlah_yang_dibeli = int(input("masukkan jumlah pesanan = "))
if beli == "a" :
  listnama = "suwar-suwir"
  harga = (17000*jumlah_yang_dibeli)
  ppn = int (harga* 0.1)
  if jumlah_yang_dibeli >= 5:
    diskon = int(harga*0.2)
    totalharga = int (harga-diskon+ppn)
  else: 
    diskon =(0)
    totalharga = int(harga+ppn)
elif beli == "b":
  listnama = "prol tape"
  harga = (20000*jumlah_yang_dibeli)
  ppn = int (harga * 0.1)
  if jumlah_yang_dibeli >= 5:
    diskon = int(harga*0.2)
    totalharga = int (harga-diskon+ppn)
  else: 
    diskon =(0)
    totalharga = int(harga +ppn)
elif beli == "c":
  listnama = "dodol tape"
  harga = (15000*jumlah_yang_dibeli)
  ppn = int (harga * 0.1)
  if jumlah_yang_dibeli >= 5:
    diskon = int(harga*0.2)
    totalharga = int (harga-diskon+ppn)
  else: 
    diskon =(0)
    totalharga = int(harga +ppn)
elif beli == "d":
  listnama = "tape besek"
  harga = (18000*jumlah_yang_dibeli)
  ppn = int (harga * 0.1)
  if jumlah_yang_dibeli >= 3:
    diskon = int(harga*0.2)
    totalharga = int (harga-diskon+ppn)
  else: 
    diskon =(0)
    totalharga = int(harga +ppn)
elif beli == "e":
  listnama = "bakpia tape"
  harga = (13000*jumlah_yang_dibeli)
  ppn = int (harga * 0.1)
  if jumlah_yang_dibeli >= 3:
    diskon = int(harga*0.2)
    totalharga = int (harga-diskon+ppn)
  else: 
    diskon =(0)
    totalharga = int(harga + ppn)

else:
  listnama = "_"
  jumlahpesan = "_"
  harga = "_"
  ppn = "_"
  diskon = "_"
  totalharga = "_"
  pilihan = input ("Menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")


print (input("barang yang dibeli:" ))
print ("harga barang :", harga)
print ("diskon :", diskon)
print ("PPN :" ,ppn)
total1 = totalharga
print ("total pembelian 1 :", total1)

pilihan = input ("-----Apakah anda ingin membeli produk makanan yang lain?------ Y/N =")
if pilihan == "N": 
  uang = int (input ("masukkan uang pembayaran :", ))
  if uang > total1 :
    print ("uang kembalian :", uang - total1)
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")
  elif uang == total1:
    print ("pembayaran pas")
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")
  else :
    print ("uangnya kurang:" , uang - total1)
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")
if pilihan == "Y":
  beli = str(input("masukkan list abjad makanan = "))
  produk = ("suwar-suwir", "prol tape", "dodol tape", "tape besek", "bakpia tape")
  jumlah_yang_dibeli = int(input("masukkan jumlah pesanan = "))
if beli == "a" :
        listnama = "suwar-suwir"
        harga = (17000*jumlah_yang_dibeli)
        ppn = int (harga* 0.1)
        if jumlah_yang_dibeli >= 5:
            diskon = int(harga*0.2)
            totalharga = int (harga-diskon+ppn)
        else: 
            diskon =(0)
            totalharga = int(harga+ppn)
elif beli == "b":
        listnama = "prol tape"
        harga = (20000*jumlah_yang_dibeli)
        ppn = int (harga * 0.1)
        if jumlah_yang_dibeli >= 5:
            diskon = int(harga*0.2)
            totalharga = int (harga-diskon+ppn)
        else: 
            diskon =(0)
            totalharga = int(harga +ppn)
elif beli == "c":
        listnama = "dodol tape"
        harga = (15000*jumlah_yang_dibeli)
        ppn = int (harga * 0.1)
        if jumlah_yang_dibeli >= 5:
            diskon = int(harga*0.2)
            totalharga = int (harga-diskon+ppn)
        else: 
            diskon =(0)
            totalharga = int(harga +ppn)
elif beli == "d":
        listnama = "tape besek"
        harga = (18000*jumlah_yang_dibeli)
        ppn = int (harga * 0.1)
        if jumlah_yang_dibeli >= 3:
            diskon = int(harga*0.2)
            totalharga = int (harga-diskon+ppn)
        else: 
            diskon =(0)
            totalharga = int(harga +ppn)
elif beli == "e":
        listnama = "bakpia tape"
        harga = (13000*jumlah_yang_dibeli)
        ppn = int (harga * 0.1)
        if jumlah_yang_dibeli >= 3:
            diskon = int(harga*0.2)
            totalharga = int (harga-diskon+ppn)
        else: 
            diskon =(0)
            totalharga = int(harga + ppn)
if pilihan == "Y":
    print (input("barang yang dibeli:" ))
    print ("harga barangnya :", harga)
    print ("diskon :", diskon)
    print ("PPN :" ,ppn)
    total2 = totalharga
    print ("total pembelian 2 :", total2)
    totalbayar = total1 + total2
    print ("total yang harus dibayar :", totalbayar)
    uang = int (input ("masukkan uang pembayaran :", ))
if uang > totalbayar :
    print ("uang kembalian :", uang - totalbayar)
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")
elif uang == totalbayar:
    print ("pembayaran pas")
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")
else :
    print ("uangnya kurang:" , uang - totalbayar)
    print ("-------------------TERIMA KASIH TELAH MEMBELI----------------------")

