def fonkisyo():
    return print("fonk calisti")

print(type(fonkisyo()))


def topla(a,b):
    print(a+b)

print("iki sayinin toplayan fonkisyon : ",topla(4,4.5))
print(type(topla(6, 3)))
print(type(topla(6, 3.5)))

def topla2(a, b):
    return a-b, a*b

print("iki sayinin ayni fonkisyon icnide iki islemini yapan : ", topla2(3, 5))

def topla_ne_varsa(*a):
    toplam = 0
    for i in a:
        toplam+=i
    return toplam

print("sinirsiz sayilarin toplayan fonkisyon : ", topla_ne_varsa(4,5,5,6,8,7,9))

def defulat(x = 6):
    if x == 6:
        print("burda defulat özelliği çalıştı : ", x)
    else:
        print("burda yazdığımız sayıyı çıkar : ", x)

defulat(9)
defulat()

def yazdir_ne_varsa(*sinirsiz):
    for i in sinirsiz:
        print(i)

print("\nburda istedigimiz her sey yazdirir : ")
yazdir_ne_varsa("bir",True,"bal",98,4j,4.56879,'Char')

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("\nfaktoriyel sayiyi uretmek : ")
def faktoriyel(sayi):
    sonuc = 1
    if (sayi == 0):
        sonuc  = 1
    else :
        while (sayi >= 1):
            sonuc = sonuc * sayi
            sayi -= 1
    return sonuc



print(faktoriyel(5))

def fonksiyon(n):
  return abs(n - 50)

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)

