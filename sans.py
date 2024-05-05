# import random

# def sans_oyunu():
#     print("Şans Oyununa Hoş Geldiniz!")

#     while True:
#         # Bilgisayar rastgele bir sayı seçer
#         bilgisayar_sayisi = random.randint(1, 100)

#         print("Bilgisayar bir sayı seçti. 1 ile 100 arasında bir sayı tahmin edin.")

#         while True:
#             try:
#                 # Kullanıcıdan tahmin al
#                 kullanici_tahmini = int(input("Tahmininiz: "))

#                 # Doğru tahmin kontrolü
#                 if kullanici_tahmini == bilgisayar_sayisi:
#                     print("Tebrikler! Doğru tahmin ettiniz.")
#                     break
#                 elif kullanici_tahmini < bilgisayar_sayisi:
#                     print("Daha yüksek bir sayı deneyin.")
#                 else:
#                     print("Daha düşük bir sayı deneyin.")
#             except ValueError:
#                 print("Geçerli bir sayı giriniz.")

#         # Yeniden oynamak isteyip istemediğini sor
#         devam_et = input("Yeniden oynamak ister misiniz? (Evet için 'e', Hayır için 'h'): ").lower()
#         if devam_et != 'e':
#             print("Oyunu İptal Ettiniz. İyi Günler!")
#             break

# if __name__ == "__main__":
#     sans_oyunu()


