'''
CEK NO HP VALID/TIDAK
syarat:
1. 081
2. panjang nomer harus 11 atau 12
'''
a = input()

cek = True
for i in range(len(a)):
    if a[0] != "0" or a[1] != "8" or a[2] != "1" or (len(a) != 12 and len(a) != 11)\
    or a[i] not in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}: 
        cek = False
    else:
        cek = True
if cek == False:
    print("invalid")
else:
    print("valid")
