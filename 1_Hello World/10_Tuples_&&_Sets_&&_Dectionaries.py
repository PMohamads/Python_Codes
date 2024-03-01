Tanitim = "1_ Tuple items are ordered, unchangeable, and allow duplicate values "
print(Tanitim)
tuple = (4, 5, 2, 6, 9, 1, 9, 'char', "metin",True)
print(tuple)
print(tuple[0])
print(tuple[1:5])
print("tupleler sıralanamaz ve hiç bir şekilde değiştirilmez ama sayıların tekrarını kabul eder ", tuple)
thistuple = ("apple", "banana", "cherry")
newlist  = []
for x in thistuple:
 if "a" in x:
    newlist.append(x)
print("Uzun yolu kullanarak :", newlist)

fruits1 = ("apple", "banana", "cherry", "kiwi", "mango")
newlist = [x for x in fruits1 if "a" in x]
print("Kisa yolu kullanarak :", newlist)

fruits2 = ("apple", "banana", "cherry")
mytuple = fruits2 * 2
print(mytuple)
#tupleri degiskenleri degistirmek istiyorsak tuple liste cevirip degistirip sonra gene tupl donustururuz

Tanitim2 = "2_ Set is a collection which is unordered(# belli bir sırası yok her defasında sırası değişyor #), unchangeable*, and unindexed. No duplicate members(# tekararlamaya izin vermez #)"
print(Tanitim2)
set = {45, 970, 'char', "str", True }
print(set)
#setleri
Tanitim3 = "3_ Dictionary is a collection which is ordered** and changeable. No duplicate members. "
dic1 = {"araba": "bmv",
        "model": 320,
        "yili": 1999}
print(dic1)
dic2 ={"araba": "dacia",
       "araba": "chevorlet",
       "model": "lasete",
       "yili": 2005}
print(dic2)
print(len(dic2))
print(dic2["model"])
dic2["motorgucu"] = "1.6"
print(dic2)
print("Burda dictionary'nin ilk siradaki degiskenlerini yansitir", dic2.keys())
print("Burda dictionary'nin ikinci siradaki degiskenlerini yansitir", dic2.values())
dic2.pop("yili")
print(dic2)
dic2.clear()
print("clear del dic2 yazarsak print(dic2) yazamayiz cunku dic2 hepsi silinmis olacak ve o yuzden hata verecek ", dic2)
dic2["araba"]= "bmv"
print(dic2)
del dic2