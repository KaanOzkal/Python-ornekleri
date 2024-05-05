class Hesapla():
    a=0
    b=0
    def topla(self,a,b):
        return a+b
    def carp(self,a,b):
        return  self.a*b
class hesapla3():
    
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Hesapla 3 classı"
    def topla(self):
        return self.a+self.b
    def carp(self):
        return  self.a*self.b

      
  


islem=Hesapla()
islem2=(20,10)
islem3=hesapla3(5,10)
# islem2.b=10
a="asd"
print(type(a),type(islem))
print(islem.topla(5,10))
print(islem.carp(5,10))
islem.a=8
print(islem.carp(5,10))

print(islem3.carp())
print(islem3.topla())
print(islem)
print(islem3)
islem3.a=2
islem3.b=3