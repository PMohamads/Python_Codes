import random

print("\n0 ile 5 arasindaki sayiler\n")
for i in range(5):
    print(i)

print("\n0 ile 5 arasindaki sayiler\n")
for i in range(0, 5):
    print("sayi : ", i)

print("\n0 ile 100 arasindaki  15 atlayarak sayiler\n")
for i in range(0, 100, 15):
    print(i)

print("\n50 ile -5 arasindaki  -5 geriye atlayrak sayiler\n")
for i in range(50, -5, -5):
    print(i)

print("\ncift sayileri cikartan\n")
for i in range(20):
    if i % 2 == 0:
        print(i)

print("\nsirasiz bir dizi icinden alsin sayisin\n")
for i in [0, 4, 3, 3]:
    print(i)

for i in range(6):
    pass

print("\nDiziler icinde donguler : ")
dizi = ["week1", "week2", 3]
dizi2 = ["monday", "tuesday", "wednesday", "thursday"]
for x in dizi:
    for y in dizi2:
        print(x, y)

for harf in "Balikesir":
    print(harf)

for harf in "Balikesir unversitesi":
    if harf == " ":
        continue
    print(harf)
    if harf == 'v':
        print("dongu durduruldu")
        break

# onemli ornek....................................................
for i in range(20):
    print("*"* i)

print(*range(0,40))
print(*range(40,0,-2))