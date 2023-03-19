faiz = 1.59
vade = "36"
krediAdi = "ihtiyaç kredisi"

print(type(vade))
print(type(faiz))

print(int(vade)+12)
print(krediAdi)
print(faiz)
faiz = str(faiz)
print(type(faiz))

vade = int(input("deger giriniz:"))
print(type(vade))
print(vade)

vade = vade + 12

#string interpolation
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = "serdar"
metin = "merhaba {name}".format(name=isim)
print(metin)


#f-string
ad="zafer"
metin=f"Hoşgeldiniz {ad}"
print(metin)


#diziler (listeler) 
#döngüler
#fonksiyonlar

krediler = ["ihtiyaç kredisi","taşıt kredisi","Konut kresisi"]
print(type(krediler))

#lenght
print(len(krediler)) 

krediler.append("Özel krediler")
print(krediler[3])

krediler.pop() #son eklenen veya eklenmiş nesneyi siler
print(krediler)

krediler.pop(0) #ilk indexi yani dizideki ilk nesneyi siler
print(krediler)

krediler.append("Sağlık kredisi")
print(krediler)

for i in range(3): #for kullanımı
    print(krediler[i]) #dizilerle ilişkilendirme

print("**************")

for i in range(0,51,10): #10'ar artırma döngüsü
    print(i)

for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])
