kartSifre = 1234
bakiye = 1000
denemeHakki = 3
kartİslemDurumu = True
print("Bankamıza Hoşgeldiniz")

islemdurumu = True
while islemdurumu:
    girilenSifre = int(input("Lütfen şifrenizi giriniz: "))  
    if girilenSifre != kartSifre:
        print("Şifreniz yanlış!")
        denemeHakki -= 1 
        print(denemeHakki, "deneme hakkınız kaldı")
        if denemeHakki == 0:
            print("Kartınız bloke edildi")
            islemdurumu = False  
    else:
        print("Giriş yapıldı")

        print("""
            Yapılacak işlemi seçiniz
            -------------------------
            1-Para çekme
            2-Para yatırma
            3-Bakiye sorgulama
            4-Çıkış
            5-Borç bilgisi
            -------------------------
            """)
        while kartİslemDurumu:
            islemNo = input("İşlem numarasını seçiniz: ")
            if islemNo == "4":
                print("Çıkış yapıldı")
                islemdurumu = False
                kartİslemDurumu = False
            elif islemNo == "3":
                print("Bakiyeniz:", bakiye, "₺")
            elif islemNo == "2":
                miktar = int(input("Yatırılacak miktar: "))
                bakiye += miktar
                print("İşlem gerçekleşti")
                print("Güncel tutarınız:", bakiye, "₺")
            elif islemNo == "1":
                miktar = int(input("Çekilecek miktar: "))
                bakiye -= miktar
                print("İşleminiz gerçekleşti")
                print("Güncel bakiyeniz:", bakiye, "₺")
            elif islemNo == "5":
                if bakiye < 0:
                    print("Borç bilgileriniz:")
                    print("Borç miktarınız:", abs(bakiye), "₺")
                else:
                    print("Borç bilginiz yoktur, bakiyeniz pozitif.")
            else:
                print("Geçersiz işlem numarası, lütfen tekrar deneyin.")

            if bakiye < 0:
                print("Dikkat! Hesabınızda borç bulunmaktadır.")
                print("Borç miktarınız:", abs(bakiye), "₺")
