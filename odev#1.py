#odev1
ogrenciList = ["servet sayar"]
def ogrencilistesi():
    for i in range(0,len(ogrenciList)):
        print(ogrenciList[i])
        

def ogrenciEkleme():
    ad = input("Ad giriniz :")
    soyad = input("Soyad giriniz :")

    ogrenciList.append(ad + " " + soyad)

def ogrenciSilme():
    silOgrenci = input("Silenek Kişinin adını ve soyadını giriniz:")
    for i in range(0,len(ogrenciList)):

        if silOgrenci in ogrenciList:
            ogrenciList.remove(silOgrenci)
            print("ogrenci başarıyla silindi")
            break
    print("silinecek kişi bulanamdı")

def ogrenciNo():
    print("ogrenci no ogrenme")
    ogrenciAd = input("Ad:")
    ogrenciSoyad= input("Soyad:")
    for i in range(0,len(ogrenciList)):

        if silenecekAd and silenecekSoyad in ogrenciList:
            print("ogrenci no: " + i)

ogrencilistesi()
ogrenciEkleme()
ogrencilistesi()
ogrenciSilme()
ogrencilistesi()
ogrenciNo()

