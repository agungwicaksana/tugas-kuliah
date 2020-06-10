import time
print('=========================================================\n')
print('              Program Input Data Mahasiswa')
print('         Muhammad Agung Wicaksana | 19.01.4281\n')
print('=========================================================\n')

data = {
    'data1' : 'Nama   :: ',
    'data2' : 'NIM    :: ',
    'data3' : 'Email  :: ',
    # tambahkan form data baru disini
}

daftarMhs = []

def inputAngka(teks):
    konst = input(teks)
    while not konst.isnumeric():
        konst = input('                Harus angka bulat! Input yang benar!\n' + teks)
    return int(konst)

play = True
def ulang():
    lagi = input('\nTambah yang lain? (y/n) >> ')
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
    jumlahMhs = inputAngka('Masukkan jumlah data yang ingin diinput  :: ')
    for i in range (0,jumlahMhs):
        print('\nData Mahasiswa ke-'+str(i+1))
        dataMhs = []
        for index in range (0,len(data)):
            inputData = input(data['data'+str(index+1)])
            dataMhs.append(inputData)
        daftarMhs.append(dataMhs)

    print('\nTerimakasih sudah input data')
    print('Ringkasan Data Mahasiswa :')
    index = 1
    for mhs in daftarMhs:
        nama, nim, email = mhs
        print(str(index)+'.',nama,'('+str(nim)+')','<'+email+'>')
        index+=1

    play = ulang()

#agung.wicaksaana@gmail.com