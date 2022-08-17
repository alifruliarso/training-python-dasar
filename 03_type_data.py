panjang = 100 # tipe data integer
lebar = 2.5 # tipe data float
nama = "aa" #tipe data string
nama2 = 'nama pake satu petik' #tipe data string
nama3 = ''' nama panjang ''' #tipe data string
is_sudah_makan = True #tipe data boolean



##Casting type data
##konvert tipe data ke bentuk yg lain
##kenapa ? gak semua sesuai kebutuhan tipe datanya

# umur = input("Isi umur\n")
# print(umur, " type nya =", type(umur))

##cara konversi ada2
##secara implisit = otomatis
# a = 10 /2
# print("a=", a, " type=", type(a))
# b = 10 + 2.0
# print("b=", b, " type=", type(b))

##cara eksplisit. Kita pannggil konstruktor dari tipe data
## konvert menjadi integer => int(x)
## konvert menjadi string => str(x)
## konvert menjadi boolean => bool(None)
## konvert menjadi float => float()

# panjang = input("input panjang:")
# lebar = input('input lebar:')
# print("panjang typenya=", type(panjang), "\n lebar typenya=", type(lebar))
# print('hitung luas =', panjang * lebar) #error karena tidak bisa multiply string
# #maka variable panjang&lebar harus di konvert ke integer sebelum dilakukan operasi multiply

# nama = 'bambang'
# tahun_lahir = 2000
# #andi lahir tahun 2000
# print(nama + " lahir tahun " + str(tahun_lahir))


##Jika dikonversi ke boolean, maka nilai yang jadi FALSE adalah berikut:
## string kosong = ""
## integer 0
## float 0.0

#print(type(True))
#var1 = 0.0
#print(var1, " boolean  =", bool(var1)) # True / False
