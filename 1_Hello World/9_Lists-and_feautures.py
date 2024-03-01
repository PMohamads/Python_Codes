a = [True, 56, .3, 'yes', "fourth", 7j, None, [5, 64, "86", 4, 79], 56]
print(a)
print(a[3])
print(a[-3])
print(a[-5:-1])
print(type(a[2]))
print(a[7][3])
print(a[7][1:5])
a[7][2] = [8, 7, 5, 4, 2, 'ttm', 4, 8]
print(a[7][2][4])
print(a[7][2][0:100])
print(type(a[7][2][5]))
print(type(a[7][2][0:9]))
print("a'nin uzunlugu ", len(a))
print("lists uzerinde islemler...")
x = ["first", "secound", "third", "fourth", "fifth"]
b =[]
for i in x :
    b.append(i.upper())
print(b)
print("x : ", x, "boyu : ", len(x))
x.append(66)
print("x1 : ", x, "boyu : ", len(x))
print(" silinecek nesne : ", x.pop())
print("x2 : ", x, "boyu : ", len(x))
x.append(66)
print("x3 : ", x, "boyu : ", len(x))
x.pop(5)
print("x4 : ", x, "boyu : ", len(x))
x.insert(1, 45)
print("x5 : ", x, "boyu : ", len(x))
del x[1]
print("x6 : ", x, "boyu : ", len(x))
x.remove("third")
print("x7 : ", x, "boyu : ", len(x))
x.insert(1, "ilki")
print("x8 : ", x, "boyu : ", len(x))
x.reverse()
print("x9 : ", x, "boyu : ", len(x))
x.sort()
print("x10 : ", x, "boyu : ", len(x))
x.clear()
print("x11 : ", x, "boyu : ", len(x))
y = [4, 5, 6, 7, 3]
x.extend(y)
print("x12 : ", x, "boyu : ", len(x))
print(x.index(6))
Q = ["Buyukharfli","kucukharfli","Smallletter","First", "apple"]
z = Q.copy()
print("z dizisi : ", z)
Q.sort(key=str.lower)
print("**** Burda tum metinleri küçük harflara çevirdi sonra sıraladı yoksa diğer türlü düzgün sıralamazdı :\n", Q)

liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
print(liste2)
liste3 = liste1.copy()
print(liste3)
del liste1

s = "Python"  # Örnek 5
liste5 = [i * 3 for i in s] # List Comprehension
print("sss",liste5)

#Örnek 5 uzun yolu
s = "Python"
liste6 = list()
for i in s:
    i *= 3
    liste6.append(i)

print(liste6)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# or .........
newlist2 = list()
for i in fruits :
    newlist2.append(i.lower())
print(newlist2)
print("\n\nfibonacci sersi uretmek ......onemli......")
"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
1,1,2,3,5,8,13,21,34...............
"""
ilk_sayı = 1

ikincisayi = 1

fibonacci = [ilk_sayı,ikincisayi]
for i in range(10):


    ilk_sayı,ikincisayi = ikincisayi,ilk_sayı + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)

x = eval(input("dizinin siniri yaziniz : "))
fdizisi = [1, 1]
for i in range(x):
    i = fdizisi[i]+fdizisi[i+1]
    fdizisi.append(i)

print(fdizisi)
