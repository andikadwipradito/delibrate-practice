from typing_extensions import Self


class Hewan :
    """class Hewan, dengan class atrribute default nama latin Animalia, dengan attribut nama dan umur.
    Selain itu class Hewan juga bisa menyesuaikan nama latin child class dengan menggunakan method change_nama_latin.
    """
    nama_latin = "Animalia"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bangun(self):
        print("*hewan ini sedang bangun dan menguap*")
    
    def change_nama_latin(self, nama_latin_baru):
        print(nama_latin_baru)
    


class Kucing(Hewan):
    def change_nama_latin(self):
        return("Felis catus")
    
    def lari(self, kecepatan):
        if kecepatan > 10:
            return("Cepat sekali")
        else:
            return("Lambat")


kit = Kucing("Muezza", 3)
print("Hallo, saya punya kucing bernama {}, dia berumur {} tahun".format(kit.nama, kit.umur))
print("Kucing itu punya nama latin yang bernama {}".format(kit.change_nama_latin()))
print("{} ini gendut, jadi lari dia {}".format(kit.nama, kit.lari(3)))