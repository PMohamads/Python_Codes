"""
faktoriyel sayiyi fonkisyon icinde uretin
"""
sayi = eval(input("Faktoriyel alacaginiz sayiyi giriniz : "))
def faktoriyel(sayi):
    sonuc = 1
    if (sayi == 0):
        sonuc  = 1
    else :
        while (sayi >= 1):
            sonuc = sonuc * sayi
            sayi -= 1
    return sonuc
print(faktoriyel(sayi))




''' 
1 - Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız
'''
liste = []
for i in range(5):
    x = eval(input("{} please enter 5 numbers".format(i)))
    liste.append(x)
liste.sort()
print(liste)



'''
while True: # Sonsuz döngü. Nasıl sonlandırabiliriz ? 
    isim = input("İsminiz(Çıkmak için q tuşuna basın.):")
    if (isim == "q"): # break ile tabii ki.
        print("Çıkış yapılıyor...")
        break
    print(isim)
'''


"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
"""
def polinDRAM(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(polinDRAM(10, 101, 55, 40, 9009))