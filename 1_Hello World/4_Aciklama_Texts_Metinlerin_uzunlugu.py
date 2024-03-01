# Bir Satırlık yorum Satırı
"""
birden fazla yorum satiri
yada
birden fazla aciklama satiri
"""
'''
cift tirnaklar gibi 
birden fazla yorum
yada 
birden fazla aciklama
satiri
'''
aciklama1 =("boyle yazilabilir")
aciklama2 = """ Strings in python are Arrays \n List is a collection which is ordered and changeable. Allows duplicate members : """
print(aciklama2)
print(aciklama1)
yorum = '''Burda yorum satirlari bir string olarak davranilir ve gorulur'''
print(yorum)
print(type(yorum))
print("yorumunun uzunlugu =", len(yorum))
print("istedimiz indeksi da secebiliriz << ", yorum[6]+yorum[7]+yorum[8]+yorum[9]+yorum[10], " >>")
string = "Hello World"
print("Metinin uzunlugu", len(string))
print(string[0])
print(string[6:])
print(string[:5])
print(string[4:11])
print(string[0:8:1])
print(string[0:8:2])
print(string[0:8:3])
print(string[0:9:4])
print(string[-11:-5])
print(string[-7:-1])
print(string[-7:-5])