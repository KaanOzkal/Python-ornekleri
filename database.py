# import sqlite3 as sql

# baglanti=sql.connect("ornek.db")   #örnek.sqllite3cd 
# cursor = baglanti.cursor()

# def tablo_olustur():
#     cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (id INTEGER,AdSoyad TEXT,yas INTEGER, PRIMARY KEY ('id' AUTOINCREMENT))")
#     baglanti.commit()
# tablo_olustur()
# def veri_ekle():
#     cursor.execute("INSERT INTO ogrenciler (AdSoyad,yas) VALUES('kaan',25)")
#     baglanti.commit()
    
# def veri_ekle():
#     cursor.execute("update ogrenciler set adSoyad='kaan' where yas='25' adSoyad='kaannnnn")
#     baglanti.commit()
#     veri_ekle()
# baglanti.commit()

# veri_ekle()




# def veri_ekle2(ad,yas):
#     cursor.execute(f"""
# insert into ogrenciler(adSoyad,yas)values ('{ad}'),{yas}
# """)

# def veri_ekle3(ad,yas):
#     cursor.execute("insert into ogrenciler(adSoyad,yas)values (?,?)",(ad,yas))
#     baglanti.commit()
# x=input("AD yaz: ")
# y=input("yas yaz: ")
# veri_ekle3(x,y)

# def veri_oku():
#     cursor.execute("select * from ogrenciler")
#     bilgiler=cursor.fetchall()
#     for i in bilgiler:
#         print(i)
# veri_oku()

# def veri_oku2():
#     cursor.execute("select * from ogrenciler")
#     bilgiler=cursor.fetchone()
#     print(bilgiler)
#     # for i in bilgiler:
#     #     print(i)
# veri_oku2()

# def veri_oku3():
#     cursor.execute("select * from ogrenciler")
#     bilgiler=cursor.fetchmany()
#     print(bilgiler)
#     # for i in bilgiler:
#     #     print(i)
# veri_oku3()


# def veri_güncelle(id,name,yas):
#     cursor.execute(f"update ogrenciler set yas={yas} where id={id}")
# baglanti.commit()
# veri_güncelle(3,"berat",99)

# def veri_sil():
#     cursor.execute("delete from ogrenciler")
#     baglanti.commit
# veri_sil()