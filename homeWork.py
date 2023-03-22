
#class
class Banka:
    def krediBasvuru(self):
        print("kredi başvuru yapıldı")
    
    def krediHesapla(self):
        print("kredi hesaplandı")

#classlarda constructer-yapıcı
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1 #constructer uygulanması
        self.sayi2 = sayi2
        print("matematik refransı verildi")
    
    def topla(self):
        return self.sayi1 + self.sayi2 

    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2

    def carp(self,sayi1,sayi2):
        return self.sayi1 * self.sayi2
    
matematik = Matematik(6,7)
sonucToplam = matematik.topla()
sonucCikar = matematik.cikar()
print("Toplam Sonuç :" + str(sonucToplam))
print("Cıkarma sonuçu :" + str(sonucCikar))
