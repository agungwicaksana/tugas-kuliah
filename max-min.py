import time
print('=========================================================\n')
print('       Program Menentukan Nilai Maksimal dan Minimal')
print('         Muhammad Agung Wicaksana | 19.01.4281\n')
print('=========================================================\n')

def inputAngka(teks):
    konst = input(teks)
    while not konst.isnumeric():
        konst = input('                Harus angka bulat! Input yang benar!\n' + teks)
    return int(konst)

def summary(grupAngka):
    total = []
    for list in grupAngka:
        total.extend(list)
    print('\nNilai maksimal (All) : ', max(total))
    print('Nilai minimal  (All) : ', min(total))

play = True
def ulang(grupAngka):
    lagi = input('\nUlangi? (y/n) >> ')
    if lagi == 'y':
        print('\n')
        return True
    elif lagi == 'n':
        summary(grupAngka)
        print('\n                 --- Terimakasih  ---\n                  --- 19.01.4281 ---\n')
        time.sleep(1.5)
        return False
    else:
        print('                                   Input yang benar!')
        return ulang(grupAngka)
grupAngka = []
putaran = 1
while(play):
    jumlahAngka = inputAngka('Masukkan jumlah data yang ingin diinput  :: ')
    grupAngka.append([])
    daftarAngka = grupAngka[putaran-1]
    for i in range (0,jumlahAngka):
        inputData = inputAngka('Masukkan angka ke ' + str(i+1) + ' :: ')
        daftarAngka.append(inputData)
    print('\nNilai maksimal : ', max(grupAngka[putaran-1]))
    print('Nilai minimal  : ', min(grupAngka[putaran-1]))
    daftarAngka = []
    putaran += 1
    play = ulang(grupAngka)

#agung.wicaksaana@gmail.com