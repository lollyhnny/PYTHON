#Deger donduren fonksiyonlar
#Deger dondurme fonksiyonu, programin onu cagiran bolumune bir deger donduren bir fonksiyondur.
# import kullanimi:
import random
def main():
   for number in range(10): #for count in range(10): da kullanabiliriz
    number=random.randint(1,100,)
    print(number)
main()
#bir F-stringden fonksiyon cagirma:

print(f' 1\'le 100 arasi rastgele bir sayi: {random.randint(1,100)} ')

# zar atma
min=1
max=6
def main2():
    tekrar='E'
    while tekrar== 'E' or tekrar=='e':
        print('Zar atiliyor...')
        print('Degerleri: ')
        print(random.randint(min,max))
        print(random.randint(min,max))
        tekrar=input('yeniden zar atmak istiyor musunuz? (Evet icin E veya e giriniz: ) ')
        
main2()      
#kendi deger donduren fonksiyonumuzu yazalim:
def main3():
    yas1=int(input('Bir yas giriniz: '))
    yas2=int(input('Bir yas giriniz: '))
    print(f'Girdiginiz yaslarin toplami: {YasToplam(yas1,yas2)} ')



def YasToplam(yas_1,yas_2):
    toplam=yas_1+yas_2
    return toplam # veya return yas_1 + yas_2 kullanabiliriz

main3()
#IPO charts : input processing ve output tanimlar 

#0'a bolum hatasi ayiklama
def main3():
    num1=int(input('Bir sayi giriniz:'))
    num2=int(input('Bir sayi giriniz:'))
    bolum=Bolum(num1,num2)
    if bolum is None:
        print('0\'a bolunemiyor...')
    else:
        print(f'{num1} \'in {num2}\'ye bolumu= {bolum}')
def Bolum(num_1,num_2):
    if num_2==0:
       return None
    else:
     return num_1/num_2

main3()
#math modulu kullanimi import math
import math
def KareAl():
    number=float(input('Bir sayi giriniz: '))
    kare=math.sqrt(number)
    print(f'{number}\'nin karesi= {kare}')

KareAl()
