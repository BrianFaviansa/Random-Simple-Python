print("=======================================")
print("    Selamat Datang di ALASKA CAFE      ")
print("=======================================")

Menu = {
    "Choco Frappe" : 25000,
    "Taro Cheese" : 18000, 
    "Red Velvet" : 20000, 
    "Caramel Latte" : 28000, 
    "Avocado Coffee" : 30000, 
    "Mango Yakult" : 15000, 
    "Ice Lychee Tea" : 15000, 
    "Hot Thai Tea" : 17000, 
}

print("======= Menu yang Kami Sediakan =======")
for i in Menu :
    print(i, "\t : ", Menu[i])

Pesan = (input("Pesanan Anda : ")) #Tulis pesanan dengan huruf besar dan kecil yang sesuai dengan menu di atas
Jumlah_Pesanan = int(input("Jumlah yang dipesan : "))
Harga = Jumlah_Pesanan*Menu[Pesan]


print("========== STRUK PEMESANAN ==========")
print("Pesanan Anda     : ", Pesan)
print("Jumlah Pesanan   : ", Jumlah_Pesanan)
print("Total Pembayaran : ", Harga)

#Pilih salah satu metode pembayaran, 1 atau 2
print("====== Pilih Metode Pembayaran ======")
print("1. Tunai")
print("2. Debit")
opsi = int(input("Pilih Opsi Pembayaran : "))

if opsi == 1 :
    print("Total Pembayaran Anda : ", Harga)
    uang_bayar = int(input("Masukkan nominal uang anda : "))
    kembali = uang_bayar - Harga 
    print("Kembalian anda adalah ", kembali)
elif opsi == 2 :
    print("Hanya menyediakan Bank BRI")
    print("Jika menggunakan Bank lain akan dikenakan biaya tambahan")
    print("Total Pembayaran Anda : ", Harga)
else :
    print("Opsi yang anda masukkan salah") 

print("========== TERIMA KASIH ==========")