import Bizim_Module
import Bizim_Module as bb
x = Bizim_Module.toplamaislemi(4,5,5,8,4,8,6)
print(x)
y = bb.cikarmaislemi(4,8,8)
print(y)

print("Burda tum dosyaiyi cagirmak yerine sadece tek islemi cagirdik ....")
from Bizim_Module import toplamaislemi
z = toplamaislemi(4,7,7,8,7,8,4,8)
print(z)
print(bb.x)