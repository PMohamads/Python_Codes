class init:
    metin = "yazilan"
    def __init__(self,a,b):
        self.adi = a
        self.soyadi = b

    def __str__(self):
        self.isim = self.soyadi
        return self.metin + self.adi + self.soyadi

nesne = init(" isimim "," soyisim ")
print(nesne)

class fwithstr:
    def __init__(ben,a,b):
        ben.adi = a
        ben.yas = b

    def __str__(self):
        self.sene = self.yas
        return  f"{self.adi}({self.sene})"

nesne4 = fwithstr("mohamad","24")
print(nesne4)
print(nesne4.adi)


class sil:
    def __str__(self):
        return 5+8
    def __del__(self):
        print("ilk sinif silindi ve asagaiya gider ama gene da tam silinmez ")

nesne3 = sil()
print(nesne3.__str__())

class delete:
    adim = "silici"
    def __init__(self,a):
        self.adim = a
    def __del__(self):
        print(self.adim + " silindi ve en sona gecti .....")

nesne2 = delete("mehaba")

class gec:
    pass

nesne5 = gec()
print("pass yazdigimiz icin sorun cikartmadi : ", nesne5)


class sinif:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __repr__ (self):
        return "MyClass(x=" + str(self.x) + ' ,y=' + self.y + ')'
myObject = sinif(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())