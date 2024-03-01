print("burda islemleri tanimladik ve bu dosayiyi cagirdigimizde ilk bu cikar ve tek seferlik cikar ...")
def toplamaislemi(*a):
    toplam = 0
    for i in a:
        toplam += i
    return toplam

def cikarmaislemi(a,b,c = 9):
    return a-b-c

x = ['tr',True,67]