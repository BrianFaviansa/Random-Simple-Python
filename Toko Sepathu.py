print ("SELAMAT DATANG DI shepathu,SELAMAT BELANJA")
print ("silahkan kak,mau cari sepatu apa?di sini kami ada beberapa jenis sepatu kak")

data_barang = "\n sneakers \n boots \n flats shoes \n sandal jepit"
print ("=====================DATA BARANG=====================: " + data_barang)
print ('untuk detail barang dan harganya seperti ini kak')
list_harga ={
  "sneakers" :150000,
  "boots" :250000,
  "flats shoes" :170000,
  "sandal jepit":39000,
}
print (list_harga)
print ('kariawan: setiap pembelian 2 sepatu sedang ada promo disc 10% kak')
print ("pembeli: baik ka,saya ingin membeli 2 sneakers ya")
list_pesan = ["2 sneakers"]
print ("kariawan: oke kak di tunggu sebentar ya!:", list_pesan)

#input pembelian
senaker=150000
jumlah=2
total= 150000*2
print ("harga awal:", total)

#setiap pembelian 2 sepatu disc 10%
diskon = float((total*10)/100)
total2 = total - diskon
print("total yang harus dibayar:", total2)

#pembayaran
print ("baik, ini uangnya 300000")
bayar= 300000-270000
print("kembali nya jadi:", bayar)
print ("terimakasih dah belanja di shepathu")