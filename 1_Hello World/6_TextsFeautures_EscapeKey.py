x = "balikesir UNVERSITESI"
print("Metinin tumu kucuk harflarle yazilir", x.lower())
print("Metinin tumu BUYUK harflarle yazilir", x.upper())
print("Metinin ilk harfi sadece BUYUK harfle yazilir kalani da kucuk yapar", x.capitalize())
print("metindeki istedigimiz harfi degistirir", x.replace("i", "efs"))
print("metindeki istedigimiz harfi indeksini verir", x.index("i"))
print("metindeki istedigimiz harfinin sayisi verir", x.count("i"))
print("metini bos olup olmadigini gosterir", x.isspace())
print("metinin onluk sayi olup olmadigini gosterir", x.isdecimal())
y = "409897"
print("metinin onluk sayi olup olmadigini gosterir", y.isdecimal())
metin = "balikesir universitesi {} yilinda kuruldu ve  {} fakulte sayisi vardir"
print("format özelligini kullanmak", metin.format(1992, "13"))
print("bilgisayar muh bolumu yilda {} ve {} arasinda ogrenci sayisi kabul ediyor".format(80, 90))
print("bilgisayar muh bolumu yilda {1} ve {0} arasinda ogrenci sayisi kabul ediyor".format(80, 90))
print("bilgisayar muh bolumu yilda %d ve %s arasinda ogrenci sayisi kabul ediyor" % (80, 899))
print("farkli yerleri siralama : {2} + {1} + {3} + {0}".format(0, 'ikinci', 2, "dordunc"))
print(f"farkli format ozelligi kullanma : {5} + {y} + {x} + {0}")
print("tekkelime".upper())
print("TEKkelime".lower())
print("tekkelime".capitalize())
print("escape anahtari kullanma \'")
print("escape anahtari kullanma \\")
print("escape anahtari kullanma \n")
print("escape anahtari kullanma \f")
print("escape anahtari kullanma i silindi\b")