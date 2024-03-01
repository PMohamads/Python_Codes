class kisi:
    metin ="dunya"
    def __init__(self, adi , yasi, a):
        self.ad = adi
        self.yas = yasi
        self.metin = a
        print("init fonkisyonu return edilmez")

sinif = kisi("mohamad", 24, "merhaba")
print(sinif.ad)
print(sinif.metin)

