toplam=5
liste=[]
for i in range(toplam):
     deger = int(input("Bir Değer Giriniz: "))
     if deger % 3 == 0:
          liste.insert(0,deger)
     else:
          liste.append(deger)
           
print("Listenin Son hali",liste)

class Kişi:
     def __init__(self,yaş,ad):
          self.yaş=yaş
          self.ad=ad
     def __str__(self):
          return f"{self.ad}{self.yaş}"
     
k1 = Kişi(ad="Abdurrahman ",yaş=17)
print(k1)

class Soru:
     def __init__(self,soru,cevap):
          self.soru=soru
          self.cevap=cevap
     def doğru_mu(self,tahmin):
          return self.cevap == tahmin
soru1=Soru("başkent neresi: ","ankara")
soru2=Soru("en kalabalık şehir neresi: ","istanbul")
soru3=Soru("en güzel şehir: ","bolu")

dogru_cevaplar=0
sorular = [soru1,soru2,soru3]
for i in sorular:
     cevap=input(i.soru)
     if i.doğru_mu(cevap):
          dogru_cevaplar+=1
print(f"doğru cevap sayısı",(dogru_cevaplar))
