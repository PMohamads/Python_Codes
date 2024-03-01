dosya = open("metin.txt", 'r')
print(dosya.read())

dosya = open("metin.txt", "a")
dosya.write("Now the file has more content!")
dosya.close()

