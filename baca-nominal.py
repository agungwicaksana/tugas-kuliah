import time
print('\n\n   --- Selamat datang di program Membaca Nominal ---')
print('-------- Muhammad Agung Wicaksana | 19.01.4281 --------\n')

def inputAngka(teks):
    konst = input(teks)
    while not konst.isnumeric():
        konst = input('                Harus angka bulat! Input yang benar!\n' + teks)
    return int(konst)

def terbilang(bil):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bil)
    if n >= 0 and n <= 11:
        Hasil = Hasil + angka[n]
    elif n < 20:
        Hasil = terbilang(n % 10) + " Belas"
    elif n < 100:
        Hasil = terbilang(n / 10) + " Puluh" + terbilang(n % 10)
    elif n < 200:
        Hasil = " Seratus" + terbilang(n - 100)
    elif n < 1000:
        Hasil = terbilang(n / 100) + " Ratus" + terbilang(n % 100)
    elif n == 1000 :
        Hasil = " Seribu"
    elif n < 2000:
        Hasil = " Seribu" + terbilang(n - 1000)
    elif n >= 2000 and n < 1000000:
        Hasil = terbilang(n/1000) + " Ribu" + terbilang(n % 1000)
    elif n >= 1000000 and n < 1000000000:
        Hasil = terbilang(n/1000000) + " Juta" + terbilang(n % 1000000)
    elif n >= 1000000000 and n < 1000000000000:
        Hasil = terbilang(n/1000000000) + " Miliar" + terbilang(n % 1000000000)
    elif n >= 1000000000000 and n < 1000000000000000:
        Hasil = terbilang(n/1000000000000) + " Triliun" + terbilang(n % 1000000000000)
    elif n == 1000000000000000:
        Hasil = 'Satu Kuardriliun'
    else:
        Hasil="Angka hanya sampai Satu Kuardriliun"
    return Hasil

def ulang():
    lagi = input('\nBuat hitungan lagi? (y/n)    >> ')
    if lagi == 'y':
        print('')
        return True
    elif lagi == 'n':
        print('\n                 --- Terimakasih  ---\n                  --- 19.01.4281 ---\n')
        time.sleep(1.5)
        return False
    else:
        print('                                   Input yang benar!')
        return ulang()

play = True
while play:
    inputNominal = inputAngka('Masukkan Nominal :: ')
    print('\nNominal   ::  {:,}'.format(inputNominal))
    print('Terbilang ::', terbilang(inputNominal))
    print('')
    play = ulang()

#agung.wicaksaana@gmail.com