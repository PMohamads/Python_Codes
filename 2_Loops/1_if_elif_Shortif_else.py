a = 100
b = 9
c = 41
d = 41
r =4
if __name__ == "__main__":
    c = 41

print("b = ", b)
if a > b:
    print("a b'den büyüktür")
    b = 77

if a < b:
    print("a b'den küçüktür")

print("b = ", b)

if a > b:
    print("a b'den büyüktür")
    b = 99

if a < b:
    print("a b'den küçüktür")

print("b = ", b)

print("\nelif ve else kullanimi .....")
if c > d:
    print("c d'den büyüktür")
elif c == d:
    print("c d'ye esitter")
else:
    print("c d'den küçüktür")

print("\nShort if kullanimi .....")
print("a ve b farklidir ") if a != b else print("a ve b esittir")
print("b c'den büyüktür")if b > c else print("b c'den küçüktür") if b < c else print("b ve c esittir")
print("a c'den buyuktur")if a > c else print("a c'den kucuktur") if a < c else print("a ve c eittir")

print("\npass ifadesı kullanimi.....")
y = 5
if y < 0:
    pass
print("\tBurda pass ifadesi olmasayidi hata verirdi")


