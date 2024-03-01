dosya = open("cop.txt", 'w')
print("burda 'w' write fonkisyonu anlamina geliyor yani dosyaya tek seferlik yazma yetkisi verir ")
print("anlamsiz",file=dosya)
dosya.close()

print("burda 'r' read fonkisyonu anlamina geliyor yani dosyaya icindeki okuma emrini veriyor ")
dosya = open("cop.txt", 'r')
print(dosya.read())

print("burda 'a' append fonkisyonu anlamina geliyor yani dosyayi her calistirdigimzde yeni string yada int ekle ")
dosya = open("cop.txt", 'a')
dosya.write("yeni ekleyenler ")
dosya.close()

from urllib.request import  urlopen
from PIL import Image
import io
url = 'https://storage.googleapis.com/fm-01/car.jpg'
img = Image.open(urlopen(url))
image = img.tobytes()
print(len(image))