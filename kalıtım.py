class canli():
    def __init__(self,tur,beslenme,cins):
        self.tur=tur
        self.beslenme=beslenme
        self.cins=cins
    def bilgilerigöster(self):
        print(f"Tür:{self.tur}\nBeslenme:{self.beslenme}\ncins:{self.cins}")

class kedi(canli):
    def __init__(self,tur,beslenme,cins,ad,renk,cinsiyet):
        super().__init__(tur,beslenme,cins)
        self.ad=ad
        self.renk=renk
        self.cinsiyet=cinsiyet
    def bilgilerigöster(self):
        super().bilgilerigöster()
        print(f"ad:{self.ad}\nRenk: {self.renk}\ncinsiyet :{self.cinsiyet}")

cat=kedi("kedigiller","Hepçil","ankara kedisi","wadu","beyaz","erkek")
cat.bilgilerigöster()