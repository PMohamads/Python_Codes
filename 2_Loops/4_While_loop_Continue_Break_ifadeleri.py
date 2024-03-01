a = 5
while a < 10:
    print("Hello", a)
    a += 1

x = 100
while x > 0:
    x -= 5
    if x < 6:
        print("x 10'den kucuktur", x)
        break
    if x == 50:
        print("x 50'ye esittir")
    elif x == 40 or x == 30 or x == 20:
        continue
    elif x == 10:
        print("x 10'a esittir")
    else:
        print("x {}'den buyuktur".format(x))



