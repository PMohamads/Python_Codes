from random import randrange

class anasinif:
    degistilmez=[]
    def topla(self,*a):
        toplam = 0
        for i in a:
            toplam += i
        print(toplam)

liste = [4,5,7,3,2]
nesne = anasinif()


sayi = eval(input("bir sayiyi giriniz "))
while sayi != 0:
    try:
        sayi = eval(input("bir sayiyi giriniz "))
    except:
        print("hatali giris yaptiniz :")
    if sayi == 0:
        print("tesekkurler")
    if sayi == 10:
        ekle = randrange(-100,100)
        anasinif.degistilmez.append(ekle)

print(anasinif.degistilmez)