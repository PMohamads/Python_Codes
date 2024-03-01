class yazdiran:
    a = 0.5
    b = False
    c = ["empty"]
    def yazdir(self):
        x = 8
        print("x = ", x, self.c)

nesne = yazdiran()
nesne.yazdir()

class sinif:
    d = 9
    v = ["Hello", "World", "Goodbye"]
    def yazdir(self,t=9):
        self.d = 78
        self.v.pop()
        self.v.reverse()
        self.d = t
        print("sonuc : ", self.v, t, self.d)

nesne2 = sinif()
nesne2.yazdir(98)
nesne2.yazdir()
nesne2.yazdir()

