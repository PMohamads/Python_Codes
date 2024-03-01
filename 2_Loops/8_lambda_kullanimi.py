fonkisyon = lambda a : a + 5
print("bir sayiyi 5 ile toplayan lambda : ", fonkisyon(4))

fonkisyon2 = lambda a , b : a+ b + 14
print("iki sayi toplayan lambda : ", fonkisyon2(-8,-6))

fonkisyon3 = lambda a, e, t, y, r: a+e+t+y+r+2
print("sinirsiz parametre alan lambda : ", fonkisyon3(3,4,5,6,7))


def fonkisyon(x) :
    return  lambda a : a + x

sonuc = fonkisyon(9)
print(sonuc(4))

#### bir diziden fonkisyonlari kullanarak enbuyuk ve enkucuk sayilari bulan fonkisyonlar
dizi = [4,5,2,5,62,1,3,5]
def enbuyuk():
    maksimum = 0
    for i in dizi:
        if i > maksimum:
            maksimum = i
    print("dizideki en buyuk sayi : ", maksimum)

def enkucuk():
    minimum = 1000
    for i in dizi:
        if i < minimum:
            minimum=i
    print("dizideki en kucuk sayi :", minimum)


enbuyuk()
enkucuk()