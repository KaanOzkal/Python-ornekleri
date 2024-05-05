# klavyeden girilern birr sayının tek mi çift mi old gösteriniz
# sayi=int(input("yaz:"))
# if sayi%2==0:
#     print("girilen sayi çift")
# else:
#     print("sayı tek")



# klavyeden girilen sayi eğer tek iste string olarak sonuna 345 sayi eklensin çift ise 125 sayisi eklensin örneğin giirelen sayi 14 iste 14124 ...vs sayının 2 katını al



# sayi=int(input("yaz:"))
# if sayi%2==0:
#     sayi1=str(sayi)+"125"
#     sayi1=int(sayi1)*2
#     print(f"{sayi1*2}")
# else :
#     print("girelen sayi tek")
#     sayi1=str(sayi)+"345"
#     sayi1=int(sayi1)*2
#     print(f"{sayi1}")

# klavyeden girilen değeri tersten yazınız


# girilen=input("yaz: ")
# ters=""

# for i in range(len(girilen)-1,-1,-1):
#         ters+=girilen[i]
# print(ters)


# klayeden girirlen değerin 1 atlayarak ekrana yazan kodu yazının

# girilen=input("yaz: ")
# atla=""
# for i in range(0,len(girilen),2):
#     atla+=girilen[i]
# print(atla)



# klavyeden girilen sayının faktöreyilni bulan programı yazınız

# sayi=int(input("yaz: "))
# deger=1
# i=1
# while i<=sayi:
#         deger*=i
#         i+=1
# print(deger)






# Klavyeden girilen bir değerin uzunluğu tek ise a ve e yi silin çift ise t ve p yi silip tekrar ekrana basan fonk yazınız


# def harfsil(cümle):
#     result=""
#     if len(cümle)%2==0:
#         for i in cümle:
#             if i=="t" or i=="T" or i=="p" or i=="P":
#                 continue
#             result+=i
#     else:
#         for i in cümle:
#                      if i=="a" or i=="A" or i=="E" or i=="e":
#                         continue
#         result+=i
#     return result
# print(harfsil(input("yaz:  ")))






# aranan_ogrenci = input ("kaan")
 
# ogrenciler = input ['berat', 'kaan', 'hasan']
# print (": " (aranan_ogrenci , ogrenciler) , end="!\n" )
 
# for ogrenci in ogrenciler:
#     if ogrenci == aranan_ogrenci:
#         print("Aranan Öğrenci Bulundu:",ogrenci)
#         break
#     print("Öğrenci:",ogrenci)
# else:
#         print("Aranan öğrenci listede bulunamadı.")


#  Klavyden 0 girilene kadar sayılsal değer alın ve girmiş oldugunuz pozitiv girmiş old değerleri çift ve tek olarak ayrı bir şekilde tutun kullanıcı 0 a bastıktan sonra tek ve çiftleri ekran da gösterin


# tek=[]
# cift=[]
# while True:
#     ...


# Klavyeden alınan değerin uzunluğu çift ise bu değerin yarısını alıp klvayeden alınan başka değeirin ilave edin ve yeni değerin kaç ader a oldugunu gösterin tek ise yarısın alın ve içersinde kaç adet p oldugunu gösteren programı yazın


# girdi=input("bir şeyler yaz: ")
# metin=[]
# if len(girdi)%2==0:
#     for i in range(int(len(girdi)/2)):
#         metin.append(girdi[i])
#     girdi2=input("Bir şeyler daha yaz: ")
#     metin.extend(girdi2.split())
#     print(metin.count("a"))
# else:
#     for i in range(int(len(girdi)/2)):
#         metin.append(girdi[i])
#     print(metin.count("p"))









# bir database oluşturun data basein adı okul ve bu data base'de kullanıcılar olarak tablanuz olarak 2 tablonuz olsun kullanıcılar da kullancı adı,id ve şifre olsun kullanıcı sisteme kullanıcı adı ve şifre yazarak girsin ve öğrenciler tablaosun da id,ad,soyad ve not olsun ekleme güncelleme yapabilsin(ekleme silme vs.) ve kullanıcı yeni bir kullanıcı oluşturabilsin. Ve çıkış işlelmi gerçekleşene kadar bu şekilde devam etsin kullanıcı 3 defa hatalı şifre girerse bloke olsun kullanıcı adı benzersiz olsun



    
# import sqlite3 as sql

# baglanti=sql.connect("okul.db")   #örnek.sqllite3cd 
# cursor = baglanti.cursor()

# def users():
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT UNIQUE, sifresi TEXT, PRIMARY KEY('id' AUTOINCREMENT))")
#     baglanti.commit()
# users()
# def ogrenciler():
#     cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (id INTEGER, isim TEXT , soyisim TEXT,note INTEGER, PRIMARY KEY('id' AUTOINCREMENT))")
#     baglanti.commit()
# ogrenciler()

# def user_register(username,password):
#     cursor.execute(f"insert into users (username,sifresi) values ('{username}','{password}')")
#     baglanti.commit()

# def ogrenci_kayıt(ad,soyad,note):
#     cursor.execute(f"insert into ogrenciler(isim,soyisim,note)values('{ad}','{soyad}','{note}')")
#     baglanti.commit()

# def ogrenci_güncelle(id,note):
#     cursor.execute(f"update ogrenciler set note={note} where id={id}")
#     baglanti.commit()

# def ogrenci_sil(id):
#     cursor.execute(f"delete from ogrenciler where id={id}")
#     baglanti.commit()

# def user_login(username,password):
#     cursor.execute(f"users,sifresi from users where kullanici_adi_soyadi='{username}' and sifresi='{password}'")

#     bilgi=cursor.fetchone()
#     if bilgi is not None:
#         return True
#     else: 
#         return False


# users()
# ogrenciler()
# count=0
# while True:
#     girdi=input("1-G Giriş yap \n2 - Yeni kullanıcı oluştur \n3 - Çıkış \n4 - Seçim yapınız ")
#     if girdi=='1':
#         kullaniciAdi=input("lütfen adınızı giriniz: ")
#         kullanicisifre=input("lütfen şifrenizi giriniz: ")
#         if user_login(kullaniciAdi,kullanicisifre)==False:
#             pass
#             print("Hatalı adı veya şifre")
#             count +=1
#     if count==3:
#         print("bloke oldunuz !")
#         break
#         continue
    
#     elif girdi=='2':
#      username=input("adınızı oluşturunuz: ")
#      userpass=input("şifre oluşturunuz: ")
#      user_register(username,userpass)
#     elif girdi=='3':
#         break
#     else:
#         print("hatalı seçim")
        