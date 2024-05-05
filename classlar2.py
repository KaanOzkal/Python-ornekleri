# class araba():
#     def __init__(self,marka,model,hp,yil):
#         self.marka=marka
#         self.model=model
#         self.hp=hp
#         self.yil=yil

#     def bilgilerigöster(x):
#         print(f"Marka:{x.marka}\nmodel:{x.model}\nhp:{x.hp}\nyil:{x.yil}")
#     def __str__(self): 
#         return self.marka

# car1=araba("BMW","5.20i","1125","2020")

# car2=araba("Mercedes-Benz","S class","400","2020")

# car3=araba("Seat","cupra","168","2015")
# car1.bilgilerigöster()
# print("----------------")
# car2.bilgilerigöster()
# print("----------------")
# car3.bilgilerigöster()
# liste=[car1,car2,car3]

# # print(liste[0])
# for i in liste:
#     print(i)



# Bir canlı class oluşturun ve bu canlıın özellliklerini krucu metot ile alın ve bu canlının cinsiyetine göre sonuna kızım yada oğlum diye ekleme yapın

# class Canli:
#     def __init__(self, ad, yas, cinsiyet):
#         self.ad = ad
#         self.yas = yas
#         self.cinsiyet = cinsiyet

#     def bilgileri_goster(x):
#         return f"Ad: {x.ad}, Yaş: {x.yas}, Cinsiyet: {x.cinsiyet}"

#     def kiz_veya_ogul_ekle(self):
#         if self.cinsiyet == "erkek":
#             return f"{self.bilgileri_goster()} - Oğlum"
#         elif self.cinsiyet == "kiz":
#             return f"{self.bilgileri_goster()} - Kızım"



# ad = input("Adınız: ")
# yas = int(input("Yaşınız: "))
# cinsiyet = input("Cinsiyetiniz (erkek/kiz): ")


# canli = Canli(ad, yas, cinsiyet)

# print(canli.kiz_veya_ogul_ekle())


#bir clas oluşturun ve içerisnde 4 işlem bulunsun ve bu işlemleri bize değer olarak geri döndürsün



class hesapla():
    def __init__(self,a,b): 
        self.a=a
        self.b=b
    def topla (self,a,b):
        return a+b
    def cikar(self,a,b):
        return a-b
    def carp (self,a,b):
        return a*b
    def böl (self,a,b):
        return a/b
islem=hesapla(5,10)
print(islem.topla(5,10))
print(islem.cikar(5,10))
print(islem.carp(5,10))
print(islem.böl(5,10))