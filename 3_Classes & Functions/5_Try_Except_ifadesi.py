metin = "yazi"
try :
    y = metin + 5
except:
    print("string ile int toplama hatasi ..")

import random
print(dir(random))

try:
    eval(input("please enter string to catch the fault.... :"))
except:
    print("you entered a false charcter .....")