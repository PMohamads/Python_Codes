a = 58
b = 32
c = 98
d = 98

print("\nAND ve OR ve IS durumlarin kullanimi.....")
if a > b and a > c:
    print("a en buyuktur")
if b < a or c < b:
    print("b a'den kucuk yada c b'den kucuk")
if c is d:
    print("c ile d aynidir")
if c is not a:
    print("c ve a ayni degildir")
else:
    print("aynidir")

dizi = ["math", "scince", "islamic", "geomtric", "ma"]
if "math" in dizi:
    print("True")
if "sc" in dizi:
    print("True")
else:
    print("False")
for dongu in dizi:
    if "ma" in dongu:
        print("True in : " + dongu)
    else:
        print("False in : "+ dongu)

yenidizi =[]
for loop in dizi:
    if 's' in loop:
        yenidizi.append(loop)

print("s harfi icindeki kelimeler : ", yenidizi)