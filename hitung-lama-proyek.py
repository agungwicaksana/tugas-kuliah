import time
print('Sebuah gedung selesai dikerjakan dalam 120 hari jika dikerjakan oleh 10 orang.\nMasukkan jumlah pekerja yang baru untuk menghitung estimasi pengerjaan gedung!')

def inputAngka(teks):
    konst = input(teks)
    while not konst.isnumeric():
        konst = input('                Harus angka bulat! Input yang benar!\n' + teks)
    return int(konst)
def ulang():
    lagi = input('\nBuat hitungan lagi? (y/n)    >> ')
    if lagi == 'y':
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
    pekerja = inputAngka('\nMasukkan jumlah pekerja      :: ')
    hasil = 10 / pekerja * 120
    print('Pekerjaan akan selesai dalam ::', round(hasil, 2), end=' hari')
    play = ulang()

#agung.wicaksaana@gmail.com