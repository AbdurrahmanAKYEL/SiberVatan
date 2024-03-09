sayı_listesi=set[233,45,777,81,99999,36,90,88,11,61]
def sayıkontrol(sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str)) == 1:
        return 1
    else:
        return 0
for sayi in sayı_listesi:
    if sayıkontrol(sayi):
        print(f"{sayi}basamakları aynı")
    else:
        print(f"{sayi}basamakları farklı")

liste = [10,20,30]
print(type(liste))

class Person:
    address="bilgi yok"
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        def intro(self):    
            print("merhaba ben"+ self.name)
p1= Person(name="ali",lastname="koç")
print(p1)
print("benim adım",p1.name,"benim soyadım",p1.lastname,"benim adresim",p1.address)

class Person:
    def __init__(self,name,lastname,address,yil):
        self.name=name
        self.lastname=lastname
        self.address=address
        self.yil=yil 
        self.yas=2024-yil
    def intro(self):    
        print("merhaba ben"+ self.name)
p2= Person(name="Abdurrahman",lastname="Akyel",address="5000 Evler",yil=2007)
print(p2)
print("benim adım",p2.name,"benim soyadım",p2.lastname,"benim adresim",p2.address,"doğum yılım",p2.yil,"yaşim",p2.yas)                   
   
class Daire:
    
    def __init__(self,r,pi):
        self.r=r
        self.pi=pi
        self.daire=2*pi*r
    def intro(self):
        print("dairenin çevresi",self.daire)
d1 = Daire(pi=3,r=2)
d1.intro()

class Daire:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def çevre_hesaplama(self):
        return 2*self.pi*self.r
    def alan_hesaplama(self):
        return self.pi*self.r*self.r
    
d2=Daire(5)
print(d2.alan_hesaplama())        
d1=Daire(5)
print(d1.çevre_hesaplama())  
   
class Square:
    def __init__(self,kenar_uzunlugu):
        self.kenar_uzunlugu=kenar_uzunlugu
    def alan_hesaplama(self):
        return self.kenar_uzunlugu ** 2     
s1=Square(6)
print(s1.alan_hesaplama())
