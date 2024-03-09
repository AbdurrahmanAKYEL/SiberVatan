
class Kişi():
     def __init__(self,ad,soyad,):
          self.ad=ad
          self.soyad=soyad
          print("kişi oluşturuldu")
     def ben_kimim(self):
          print("ben kişiyim")

          
          
class Ogretmen(Kişi):
     def __init__(self,ad,soyad,branş):
          self.branş=branş
          Kişi.__init__(self,ad,soyad)
          # yada super().__init__(ad,soyad) self kullanmaya gerek yok
          print("Öğretemen oluşturuldu")
     def ben_kimim(self):
          print("Ben Öğretmenim")
          


class Ogrenci(Kişi):    
     def __init__(self,ad,soyad,okul_no,):
          self.okul_no=okul_no
          Kişi.__init__(self,ad,soyad)
          print("öğrenci oluşturuldu")
     def ben_kimim(self):
          print("Ben Öğrenciyim")
          
k1= Kişi(ad="Abdurrahman",soyad="Akyel")
print(k1)

o1= Ogretmen(ad="Abdulkadir",soyad="Binan",branş="Yazılım Mühendisi")
print(o1)

ö1= Ogrenci(ad="Yusuf",soyad="Muhammed",okul_no=367)
print(ö1)

k1.ben_kimim()
o1.ben_kimim()
ö1.ben_kimim()  #overrading

class İşlem():
     def __init__(self,sayı1,sayı2):
          self.sayı1=sayı1
          self.sayı2=sayı2
          
     def hesaplama(self):
          pass
          
class Toplama(İşlem):
     
     def hesaplama(self):
          print(self.sayı1 + self.sayı2)
     
class Cıkarma(İşlem):
     
     def hesaplama(self):
          print(self.sayı1 - self.sayı2)
          
class Bölme(İşlem):
   
     def hesaplama(self):
          print(self.sayı1 / self.sayı2)
          
class Carpma(İşlem):
    
     def hesaplama(self):
          print(self.sayı1 * self.sayı2)     

T = Toplama(2,5).hesaplama()
C = Cıkarma(10,7).hesaplama()
B = Bölme(100,10).hesaplama()
A = Carpma(3,50000).hesaplama()
