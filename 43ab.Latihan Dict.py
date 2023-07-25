import datetime
import os
import string
import random


# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11),
}
# buat dict kosong
data_mahasiswa = {}

while True :
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    # ngambil data dr user 
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM Mahasiswa : ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus : "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY  = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    # artinya adalah bikin key dengan random memilih string dr kode ascii uppercase 6 kali
    data_mahasiswa.update({KEY:mahasiswa})

    # dari tutor sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<15} {'SKS Lulus':<10}{'Tanggal Lahir':<10}")
    print("-"*65)
    
    for mahasiswa in data_mahasiswa :
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<15} {SKS:^10} {LAHIR:<10}")
    print("\n")
    beres = input("Lanjut gak bro? (y/n) : ")
    if beres == "n":
        break

print("\nAkhir dari program, terima kasih")




































