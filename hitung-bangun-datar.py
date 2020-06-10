import time
import math
print('=========================================================\n')
print('       Program Hitung Luas/Keliling Bangun Datar')
print('         Muhammad Agung Wicaksana | 19.01.4281\n')
print('=========================================================\n')


def inputAngka(teks):
    konst = input(teks)
    while not konst.isnumeric():
        konst = input('                Harus angka bulat! Input yang benar!\n' + teks)
    return float(konst)

def pilihBangun():
    print('Pilih jenis bangun datar:')
    print('1. Persegi\n2. Lingkaran\n3. Segitiga sama sisi/sama kaki\n4. Segitiga siku-siku\n5. Trapesium sama kaki\n6. Belah ketupat')
    pilihan = inputAngka('\nPilih angka :: ')
    print('\n')
    return pilihan


def persegi(sisi, rumus):
    if rumus == 1:
        return sisi**2
    elif rumus == 2:
        return sisi *4
    else:
        formula = rumus
        side = sisi
        hasil = persegi(side, formula)
        return hasil

def lingkaran(jari, rumus):
    if(jari % 7 == 0):
        phi = 22/7
    else:
        phi = 3.1414
    if rumus == 1:
        return phi * jari**2
    elif rumus == 2:
        return 2 * phi * jari
    else:
        r = jari
        formula = rumus
        hasil = lingkaran(r, formula)
        return hasil

def segitga(alas, tinggi, jenis, rumus):
    if rumus == 1:
        return alas * tinggi / 2
    elif rumus == 2:
        if(jenis == 'siku'):
            c = alas**2 + tinggi**2
            hasil = math.sqrt(c)
            keliling = alas + tinggi + c
            return  keliling
        else:
            a = alas / 2
            c = a**2 + tinggi**2
            hasil = math.sqrt(c)
            keliling = alas + (hasil * 2)
            return keliling
    else:
        als = alas
        tg = tinggi
        jns = jenis
        formula = rumus
        hasil = segitga(als, tg, jns, formula)
        return hasil

def trapesium(sisi1, sisi2, tinggi, rumus):
    if rumus == 1:
        luas = (sisi1 + sisi2) * tinggi / 2
        return luas
    elif rumus == 2:
        if sisi1 > sisi2:
            sisiPanjang = sisi1
            sisiPendek = sisi2
        else:
            sisiPanjang = sisi2
            sisiPendek = sisi1
        a = (sisiPanjang - sisiPendek) / 2
        b = tinggi
        c = a**2 + b**2
        hasil = math.sqrt(c)
        keliling = sisiPanjang + sisiPendek + (2 * hasil)
        return keliling
    else:
        sisiA = sisi1
        sisiB = sisi2
        height = tinggi
        formula = rumus
        hasil = trapesium(sisiA, sisiB, height, formula)
        return hasil

def belahKetupat(diagonal1, diagonal2, rumus):
    if rumus == 1:
        luas = diagonal1 * diagonal2 / 2
        return luas
    elif rumus == 2:
        a = diagonal1 / 2
        b = diagonal2 / 2
        c = a**2 + b**2
        hasil = math.sqrt(c)
        keliling = hasil * 4
        return keliling
    else:
        diag1 = diagonal1
        diag2 = diagonal2
        formula = rumus
        hasil = belahKetupat(diag1, diag2, formula)
        return hasil

def hitungApa():
    print('\nApa yang ingin dihitung?\n1. Luas\n2. Keliling')
    rumus = inputAngka('\nPilih angka :: ')
    if rumus == 1:
        print('\nAnda memilih Luas')
    elif rumus == 2:
        print('\nAnda memilih Keliling')
    else:
        print('                                   Input yang benar!\n')
        rumus = hitungApa()
    return rumus


def tanyaBangun():
    tanya = pilihBangun()
    if(tanya > 6 or tanya < 1):
        print('                                   Input yang benar!\n')
        tanya = tanyaBangun()
        return tanya
    else:
        return tanya
   
play = True
def ulang():
    lagi = input('\nBuat hitungan lagi? (y/n) >> ')
    if lagi == 'y':
        print('\n')
        return True
    elif lagi == 'n':
        print('\n                 --- Terimakasih  ---\n                  --- 19.01.4281 ---\n')
        time.sleep(1.5)
        return False
    else:
        print('                                   Input yang benar!')
        return ulang()


while(play):
    inputBangun = tanyaBangun()
    if inputBangun == 1:
        print('Anda memilih Persegi')
        sisi = inputAngka('Masukkan sisi persegi :: ')
        rumus = hitungApa()
        hasil = persegi(sisi, rumus)
    elif inputBangun == 2:
        print('Anda memilih Lingkaran')
        jari = inputAngka('Masukkan jari-jari :: ')
        rumus = hitungApa()
        hasil = lingkaran(jari, rumus)
    elif inputBangun == 3 or inputBangun == 4:
        if inputBangun == 4:
            print('Anda memilih Segitiga siku-siku')
            jenis = 'siku'
        else:
            print('Anda memilih Segitiga sama sisi/sama kaki')
            jenis = 'nonSiku'
        alas = inputAngka('Masukkan alas   :: ')
        tinggi = inputAngka('Masukkan tinggi :: ')
        rumus = hitungApa()
        hasil = segitga(alas, tinggi, jenis, rumus)
    elif inputBangun == 5:
        print('Anda memilih Trapesium')
        sisi1 = inputAngka('Masukkan panjang sisi pertama :: ')
        sisi2 = inputAngka('Masukkan panjang sisi kedua   :: ')
        tinggi = inputAngka('Masukkan tinggi trapesium     :: ')
        rumus = hitungApa()
        hasil = trapesium(sisi1, sisi2, tinggi, rumus)
    elif inputBangun == 6:
        print('Anda memilih Belah ketupat')
        diagonal1 = inputAngka('Masukkan diagonal pertama :: ')
        diagonal2 = inputAngka('Masukkan diagonal kedua   :: ')
        rumus = hitungApa()
        hasil = belahKetupat(diagonal1, diagonal2, rumus)
    else:
        break
    
    pembulatan = round(hasil,2)
    print('Hasilnya adalah           >> {:,} <<'.format(pembulatan))
    play = ulang()

#agung.wicaksaana@gmail.com