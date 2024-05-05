# for i in range(10):
#     print(i)

# for i in range(1,5,-1):
#     print(i)


# isim="kaan özkal"
# for i in isim:
#     print(i)

# i=0
# while i<=10:
#     print(i)
#     i+=1


# continue ve break komutları

# for i in range(3):
#     for j in range(5):
#         if j==2:
#          continue
#     print(f"i: {i} j: {j}")



# for i in range(10):
#     if i==5:
#         break
#     print(i)


# for i in range(3):
#     for j in range(5):
#         if j==2:
#             break
#         print(f"i: {i} j: {j}")




# Klavyeden alınan bir değerinin a bulunuyorsa a yazılmıcak a harici yazılıcak


# isim=(input("yaz: "))
# let=""
# for i in isim:
#     if i=="a" or i=="A":  
#         continue
#     let+=i
# print(let)


# bir atm düşünelim para yatırma işlemleri olsun ve bir şifre oldusun şifre 3 hakkı olsun
# kart yanlış girirese blok olsun bakiye 20k olsun yaptgınız işlemelere göre bakiyeniz güncellensin
# ve biz çıkış yapana kadar program devam etsin


count=0
sifre="1234"
count=0
bakiye=2000
while True:
    sifre=input("şire giriniz")
    if count==3:
        print("kartınız bloke oldu")
        break
    if sifre !="1234":
        count+=1
        continue
    while True:
        secim=input("\tMenu \nBakyieniz:{bakiye} \n1 -para çekme \n2 para yatırma \n0 -çıkış")
        if secim=="1":
            girdi=int(input("lütfen çekmek istediğiniz miktarı giriniz:  "))
            if girdi >bakiye:
                print("yetersiz bakiye")
            else:
                bakiye-=girdi
        elif secim=="2":
            girdi=int(input("yatımak istediğniz miktarı giriniz: "))
            bakiye+=girdi
        elif secim=="0":
            print("çıkış yapılıyor")
        break
    else:
        print("hatalı işlem")
    break

    