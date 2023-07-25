import random as rd
import os
os.system('cls')

angka = rd.randint(1,10)

while True:
    tebak = int(input('tebak angkanya : '))
    if tebak > angka:
        print(f'tebakanmu terlalu tinggi')
    elif tebak < angka:
        print(f'tebakanmu terlalu rendah')
    elif tebak == angka:
        print(f'tebakanmu benar')
        break