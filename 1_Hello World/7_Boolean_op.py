x = 0
print(bool(x))
x = 5
print(bool(x))
print(bool(13 < 23))
print(bool(13 < 2))
print(bool(3 == 5))
print(3 == 3)
print(3 <= 3)
print(3 >= 3)
y = 4 < 6
print(y)
z = 4 == 5
print(z)
w = 4 != 5
print(w)
print("7'nin tumleyeni =",~7)
t = [16, 25, 45, 63, 42]
f = 6 in t
print(25 in t)
print(f)
a = 4
b = 5
print(a < 5 or b < 5)
print(a <= 5 and b >= 5)
print(a is b)
print(a is not b)
c = ["apple", "banana"]
print("banana" in c)
print("ana" not in c)
d = ["balikesir"]
print("bal" in d)
print("BAL" in d)
print("BAL"not in d)
for i in d :
    print("burda harflara tek tek bakar : ","bal" in i)
