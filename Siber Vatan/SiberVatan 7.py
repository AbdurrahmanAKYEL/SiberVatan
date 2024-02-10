# def selamdunya():
#     print("helloworld")
    
    
# selamdunya()

# def hosgeldin(name):
#     print("hosgeldin "+name)
# hosgeldin(input("Bir İsim Gir:"))

# def fonksiyon(sehir = "konya"):
#     print("En Sevdiğim Şehir "+ sehir)
# fonksiyon("İstanbul")
# fonksiyon()
    
# def sayi(x):
#     x= x+5
#     return x
# sonuc = sayi(10)
# print(sonuc)

# def sayi(x,y):
#     return x + y
# print(sayi(8,9))

# def fonk_tuple(*argv):
#     for arg in argv:
#         print(arg)
# fonk_tuple("selam ","naber ","nasılsın ","iyidir ")

# def cift_sayilar_bul(sayi):
#     cift_sayilar = []
#     for i in range(0, sayi+1,2):
#         cift_sayilar.append(i)
#     return  cift_sayilar

# sayi = (int(input("bir sayi girin ")))
# cift_sayilar_list = cift_sayilar_bul(sayi)
# print(cift_sayilar_list)

# def toplam(sayi1,sayi2):
#     print(sayi1,sayi2)
    
# devam_etsinmi=True
# while (devam_etsinmi):
#     print("*-*-*-*-*Hoşgeldinizı*-*-*-*-**-")
#     sayi1=int(input("Sayı Girin:"))
#     sayi2=int(input("Sayı Girin:"))
#     print("Toplama için 1")
#     print("Çıkarma için 2")
#     print("Çarpma için 3")
#     print("Bölme için 4")
#     print("Çıkmak için 5")

#     seçenek=int(input("Lütfen Bir Sayı Girin:"))
#     if seçenek==1:
#         sayi1=int(input("Sayı Girin:"))
#         sayi2=int(input("Sayı Girin:"))
#         print(sayi1+sayi2)
#     elif(seçenek==2):
#         print(sayi1-sayi2)

#     elif(seçenek==3):
#         print(sayi1*sayi2)
        
#     elif(seçenek==4):
#         print(sayi1/sayi2)
#     elif(seçenek==5):
#         devam_etsinmi=False
#     else:
#         print("Lütfen Geçerli Bi Sayı Giriniz")

# def toplam(sayi1,sayi2):
#     print(sayi1+sayi2)

# def cıkartma(sayi1,sayi2):
#     print(sayi1-sayi2)

# def carpma(sayi1,sayi2):
#     print(sayi1*sayi2)

# def bolme(sayi1,sayi2):
#     print(sayi1/sayi2)
 
# devam_etsinMi = True



# while devam_etsinMi :

#     print("Toplama için 1")
#     print("Çıkarma için 2")
#     print("Çarpma için 3")
#     print("Bölme için 4")
#     print("Çıkmak için 5")
#     islem = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz"))
#     if islem == 1:
#         sayi1=float(input("ilk sayıyı giriniz"))
#         sayi2=float(input("ikinci sayıyı giriniz"))
#         print("Sonuç ",toplam(sayi1,sayi2))
#     elif islem==2:
#         sayi1=float(input("çıkaracağınız ilk sayıyı giriniz"))
#         sayi2=float(input("çıkaracak sayıyı giriniz"))
#         cıkartma(sayi1,sayi2)
#     elif islem==3:
#         sayi1=float(input("carptığınız ilk sayıyı giriniz"))
#         sayi2=float(input("iki sayıyı giriniz"))
#         sonuc=carpma(sayi1,sayi2)
#         print("Carpmadan elde edilen sonuç",sonuc)
#     elif islem==4:
#         sayi1=float(input("bölenlerden birini giriniz"))
#         sayi2=float(input("diğer böleni giriniz"))
#         if sayi2!=0:
#             print("Bir sayı sıfıra bölünebilir.")
#         else:
#             print("Sonuç",sayi1/sayi2)
#     elif islem==6 :
#         faktöriyel_ekle
#     else:
#         devam_etsinMi = False
