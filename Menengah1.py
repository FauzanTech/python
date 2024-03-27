# Filter function
# Memerlukan 2 parameter/argumen -> 1. function 2. data->array, iterasi
def function1():
    def add7(x):
        return x+7

    arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    arr2 = tuple(filter(lambda x:x%2 != 0, arr))
    arr3 = tuple(map(add7, filter(lambda x:x%2 == 0, arr)))
    print(arr)
    print(arr2)
    print(arr3)

# Optional Parameters -> Default Parameters
# def Print(word, kali=1):
#     print(word*kali)

# Print("Fauzan ")
def mobil():
    class Mobil(object):
        def __init__(self, nama, merek, tahun, kondisi="Baru", km=0):
            self.nama = nama
            self.merek = merek
            self.tahun = tahun
            self.kondisi = kondisi
            self.km = km

        def display(self, all=True):
            if all:
                print("Nama mobil: %s \nMerek mobil: %s \nTahun: %s \nKondisi: %s \nKm: %skm" % (self.nama, self.merek, self.tahun, self.kondisi, self.km))
            else:
                print("Nama mobil: %s \nMerek mobil: %s \nTahun: %s" %(self.nama, self.merek, self.tahun))

    civic = Mobil("Civic", "Honda", 2021)
    civic.display(False)
        
