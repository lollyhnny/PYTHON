#files and exceptions 
#dosya acma
#file_variable = open(filename, mode)

#dosya modlari
# 'r' (reading only) dosya degistirilemez ve dosyaya yazilamaz
# 'w' yazmak icin dosyayi acar. dosya zaten mevcutsa dosyanin icerigini siler degilse ona yazar.
# 'a' yazilacak dosyayi acar. dosyaya yazilan tum veriler dosyanin sonuna eklenir.

# Bir dosyanin konumunu belirtme
# test_file = open(r'C:\Users\Blake\temp\test.txt', 'w')

#Dosyaya yazma
def main():
    dosya = open('filozoflar.txt','w')
    dosya.write('John Locke\n')
    dosya.write('David Hume\n')
    dosya.write('Edmund Burke\n')
    dosya.close()
    dosya= open('filozoflar.txt','r')
    dosya_icerik= dosya.read()
    dosya.close()
    print(dosya_icerik)

main()

def main2():
    print('3 arkadasinizin isimlerini giriniz: ')
    isim1=input('lutfen ilk arkadasinizin ismini giriniz: ')
    isim2=input('lutfen ikiknci arkadasinizin ismini giriniz: ')
    isim3=input('lutfen ucuncu arkadasinizin ismini giriniz: ')
    dosyam= open('arkadaslar.txt','w')
    dosyam.write(isim1 + '\n')
    dosyam.write(isim2 + '\n') #name1= name1.rstrip('\n) kullanarak stringleri ayirabiliriz.
    dosyam.write(isim3 + '\n')
    dosyam.close()
    print('Isimler dosyaya yazildi')
main2()

#Var olan bir dosyaya veri ekleme:
dosyam=open('arkadaslar.txt','a')
dosyam.write('Birsen\n')
dosyam.close()

#numerik veriler icin
def main3():
    dosyam2=open('sayilar.txt','r')
    num1=int(dosyam2.readline()) #Dosyadaki verileri satir satir okur.
    num2=int(dosyam2.readline())
    num3=int(dosyam2.readline())
    num4=int(dosyam2.readline())
    dosyam2.close()
    toplam = num1 + num2 + num3 + num4
    print(f'Dosyadaki sayilarin toplami= {toplam}')
main3()

# donguleri kullanarak doya isleme
def satis():
    gun_sayisi=int(input('Satis yaptiginiz gun sayisi: '))
    satis_dosyasi=open('satislar.txt','w')
    for gun in range(1 , gun_sayisi + 1):
        satis = float(input(f'{gun}. gun icin satis miktarini giriniz: '))
        satis_dosyasi.write(f'{satis}\n')
    satis_dosyasi.close()
    print('Girdiginiz veriler dosyaya yazildi..')
satis()

# dongu kullanarak dosya okuma ve dosyanin sonunu tespit etme:
def satis_():
    satis_=open('satislar.txt','r')
    satir = satis_.readline()
    while satir != '':
       tutar = float(satir)
       print(f'{tutar:.2f}')
       satir= satis_.readline() # siradaki satiri oku
    satis_.close()
satis_()

#satirlari okumak icin for dongusu kullanimi:
def Yazarlar():
    dos=open('yazarlar.txt','r')
    print('***YAZARLAR***')
    for satir in dos:
        
        print(satir )
    dos.close()
Yazarlar()

#kAYIT ISLEME:
# bu program kullanicidan calisan verilerini alir ve bunu calisan.txt dosyasina kaydeder.
def Calisan():
    kayit_sayisi= int(input('Kac tane calisan kaydi olusturmak istiyorsunuz: '))
    dos1= open('calisan.txt','w')
    for i in range(1,kayit_sayisi + 1):
        print(f'{i}. elemaninin verilerini giriniz. ')
        isim = input(' Isim : ')
        id_num = input('ID numarasi: ')
        dep = input('Departmani: ')
    
        dos1.write(isim + '\n')
        dos1.write(id_num + '\n')
        dos1.write(dep + '\n')
        print()
    dos1.close()
    print('Veriler dosyaya kaydedildi...')
Calisan()
