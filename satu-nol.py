for i in range(0,5):
    for j in range(0,5):
        if(0 < i < 4 and j == 0):
            print('0 ', end='')
        elif(0 < i < 4 and j == 4):
            print('0 ', end='')
        elif(i == 2 and j % 2 != 0):
            print('0 ', end='')
        else:
            print('# ', end='')
    print('')

# Atau yang ini
# for i in range(0,5):
#     for j in range(0,5):
#         if((i+j)== 4):
#             print('# ', end='')
#         elif(j==2):
#             print('# ', end='')
#         elif(i==0 or i == 4):
#             print('# ', end='')
#         elif(i==j):
#             print('# ', end='')
#         else:
#             print('0 ', end='')
#     print('')

#agung.wicaksaana@gmail.com