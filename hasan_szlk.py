szlk = {
    "morning": ("sabah",),
    "brought": ("getirdi",),
    "happiness": ("mutluluk",),
    "sunny": ("güneşli",),
    "children": ("çocuklar",),
    "played": ("oynadı",),
    "birds": ("kuşlar",),
    "sang": ("şarkı söyledi",),
    "flowers": ("çiçekler",),
    "bloomed": ("açtı",),
    "wind": ("rüzgar",),
    "whispered": ("fısıldadı",),
    "through": ("arasından",),
    "trees": ("ağaçlar"),
    "sabah": ("morning",),
    "getirdi": ("brought",),
    "mutluluk": ("happiness",),
    "güneşli": ("sunny",),
    "çocuklar": ("children",),
    "oynadı": ("played",),
    "kuşlar": ("birds",),
    "şarkı söyledi": ("sang",),
    "çiçekler": ("flowers",),
    "açtı": ("bloomed",),
    "rüzgar": ("wind",),
    "fısıldadı": ("whispered",),
    "arasından": ("through",),
    "ağaçlar": ("trees",)
}

def kelime_cevir(*args, detay=False):
    for kelime in args:
        anlam = szlk.get(kelime.lower(), ("anlamı bulunamadı",))
        if detay and len(anlam) > 1:
            print(f"{kelime}: {anlam[0]} ({anlam[1]})")
        else:
            print(f"{kelime}: {anlam[0]}")

kullancisi_girisi = input("Bir cümle giriniz: ")
kelimler = kullancisi_girisi.split()
kelime_cevir(*kelimler, detay=True)
