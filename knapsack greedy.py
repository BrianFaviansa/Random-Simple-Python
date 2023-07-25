# fungsi knapsack greedy 0/1
import os 
os.system('cls')

def knapsackGreedy():
    print('Knapsack Greedy 0/1\n')

    # wadah untuk menampung data barang
    array = []
    
    # user input 
    jumlah = int(input('jumlah barang : '))
    for i in range(jumlah):
        print(f'barang ke-{i+1}')
        nama = input('nama barang : ')
        berat = float(input('berat barang (kg) : '))
        harga = float(input('harga barang (Rp) : '))
        value = harga / berat
        print('\n')

        # tampung barang sebagai dictionary
        array.append(
            {
                'nama barang' : nama,
                'berat' : berat,
                'harga' : harga,
                'value' : value
            }
        )

    # urutkan barang 
    array.sort(key = lambda x : x['value'], reverse=True)
    print('='*90)
    print('No.\tNama Barang\tBerat Barang(Rp)\tHarga Barang(Kg)\tValue')
    for i in array:
        print('{}.\t{}\t\t{}\t\t\t{}\t\t{}'.format(array.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
    print('='*90)

    # operasi knapsack 
    knapsack = []
    harga_masuk = 0
    berat_masuk = 0
    kapasitas = int(input('kapasitas knapsack : '))
    for i in array:
        if kapasitas >= i['berat']:
            if i['value'] > 0:
                kapasitas -= i['berat']
                harga_masuk += i['harga']
                berat_masuk += i['berat']
                knapsack.append(i)

    # hasil knapsack
    print('\nHasil Knapsack Greedy 0/1')
    print('='*90)
    print('No.\tNama Barang\tBerat Barang(Rp)\tHarga Barang(Kg)\tValue')
    for i in knapsack:
        print('{}.\t{}\t\t{}\t\t\t{}\t\t{}'.format(knapsack.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
    print('='*90)
    print(f'berat barang yg masuk : {berat_masuk} kg')
    print(f'sisa kapasitas knapsack : {kapasitas}')
    print(f'total harga : Rp{harga_masuk}')

# fractinal knapsack        
def fractionalKnapsackGreedy():
    print('Fractional Knapsack Greedy')

    # wadah untuk menampung data barang
    array = []

    # user input 
    jumlah = int(input('jumlah barang : '))
    for i in range(jumlah):
        print(f'barang ke-{i+1}')
        nama = input('nama barang : ')
        berat = float(input('berat barang (kg) : '))
        harga = int(input('harga barang (Rp) : '))
        value = harga // berat
        print('\n')

        # tampung barang sebagai dictionary
        array.append(
            {
                'nama barang' : nama,
                'berat' : berat,
                'harga' : harga,
                'value' : value
            }
        )

    # urutkan barang 
    print('='*90)
    print('No.\tNama Barang\tBerat Barang(Kg)\tHarga Barang(Rp)\tValue')
    for i in array:
        print('{}.\t{}\t\t{}\t\t\t{}\t\t\t{}'.format(array.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
    print('='*90)
    array.sort(key = lambda x : x['value'], reverse=True)

    # operasi knapsack 
    knapsack = []
    harga_masuk = 0
    berat_masuk = 0
    kapasitas = int(input('kapasitas knapsack : '))    
    for i in array:
        if kapasitas >= i['berat']:
            if i['value'] > 0:
                kapasitas -= i['berat']
                harga_masuk += i['harga']
                berat_masuk += i['berat']
                knapsack.append(i)
        
        elif kapasitas < i['berat']:
            i['berat'] = kapasitas
            i['harga'] = i['berat'] * i['value']
            kapasitas = 0
            harga_masuk += i['harga']
            berat_masuk += i['berat']
            knapsack.append(i)
            if kapasitas == 0:
                break

    # hasil knapsack 
    print('\nHasil Fractional Knapsack Greedy')
    print('='*90)
    print('No.\tNama Barang\tBerat Barang(Kg)\tHarga Barang(Rp)\tValue')
    for i in knapsack:
        print('{}.\t{}\t\t{}\t\t\t{}\t\t\t{}'.format(knapsack.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
    print('='*90)
    print(f'berat barang yg masuk : {berat_masuk} kg')
    print(f'sisa kapasitas knapsack : {kapasitas}')
    print(f'total harga : Rp{harga_masuk}')
        
# knapsackGreedy()
fractionalKnapsackGreedy()