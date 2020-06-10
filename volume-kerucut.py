import time
print('\n\n--- Selamat datang di program hitung volume Kerucut ---')
print('-------- Muhammad Agung Wicaksana | 19.01.4281 --------\n')
play = True

def tanya():
    lagi = input('Hitung lagi? (y/n)         >> ')
    
    if(lagi == 'y'):
        print('\n')
        return True
    elif(lagi == 'n'):
        print('\n                 --- Terimakasih ---\n')
        time.sleep(1.5)
        return False
    else:
        return tanya()

while(play):
    def masukan(teks):
        konst = input(teks)
        while not konst.isnumeric():
            konst = input('                                   Inputkan bil. bulat!\n' + teks)        
        return float(konst)

    diameter = masukan('Masukkan diameter kerucut: >> ')
    tinggi   = masukan('Masukkan tinggi kerucut:   >> ')

    radius   = diameter/2
    if(radius % 7 == 0):
        phi = 22/7
    else:
        phi = 3.1414
    hasil =  phi * radius**2 * tinggi / 3
    pembulatan = round(hasil,2)
    print('Hasilnya adalah            >> {:,} <<\n'.format(pembulatan))
    play = tanya()

#agung.wicaksaana@gmail.com