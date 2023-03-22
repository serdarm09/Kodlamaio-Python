#class

from telnetlib import AYT


def selamver():
    print("selam")


def hesaplama():
    ayFaiz = 0.02
    bakiye = 10000
    
    ay = int(input("Kac ay vadeli yatıracaksınız :"))
    for i in range(0,ay):
      sonuc = bakiye * ayFaiz
      bakiye = bakiye + sonuc
   

    print(bakiye)

hesaplama()