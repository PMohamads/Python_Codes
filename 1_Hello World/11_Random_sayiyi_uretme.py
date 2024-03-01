print("Python'da rasgele sayiyi uretmek icin bi kac yolu var")
from  random import randrange
rasgele = randrange(0,11)
print("Burda 0 ile 11 arasinda sadece sayialar cikar 0 ve 11 cikmaz : ", rasgele)
from numpy import random
rasgele2 = random.randint(0,15,size=(4))
print("Burda 1 ile 15 arasinda dizi icinde 4 tane sayialar cikar 1 ve 15 dahil : ", rasgele2)
rasgele2 = random.randint(15,size=(4,2))
print("Burda 1 ile 15 arasinda dizi icinde 2 tane sayialar cikar 1 ve 15 dahil 4 kere cikar : \n", rasgele2)
rasgele2 = random.randint(15,size=(4,2,2))
print("Burda 1 ile 15 arasinda dizi icinde 2*2 dizili sayialar cikar 1 ve 15 dahil 4 kere cikar : \n", rasgele2)
rasgele3 = random.rand(2)
print("Burda 0 ile 1 arasinda float sayialar 2 kere : \n", rasgele3)
rasgele3 = random.rand(2,2)
print("Burda 0 ile 1 arasinda float sayialar ikili diziler 2 kere rasgele eder: \n", rasgele3)
import  random
rasgele2 = random.randint(1,10)
print("Burda 1 ile 10 arasinda sadece sayialar cikar 1 ve 10 dahil : ", rasgele2)
rasgele3 = random.random()
print("Burda 0 ile 1 arasinda sadece Float sayialar cikar :", rasgele3)
rasgele_list = ["first", "secound", "third", "fourth"]
rasgele4 = random.sample(rasgele_list, k=1)
print("Burda Dizilerden yada Tuplelerden yada Dictionlerden istedigimiz sayida rasgele bir nesne alir : ", rasgele4)
rasgele_tuple=(56,'rasgele', "random")
rasgele5 = random.choice(rasgele_tuple)
print("Burda Dizilerden yada Tuplelerden yada Dictionlerden rasgele bir nesne alir : ", rasgele5)
rasgele6 = random.shuffle(rasgele_list)
print("Burda ayni diziyi geri donduryor ama farkli sirada : ", rasgele_list)


