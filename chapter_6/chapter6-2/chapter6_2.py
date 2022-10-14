# kayit arama:
def KayitEkle():
 devam = 'e'


 kahve_dos = open('coffee.txt', 'a')

 
 while devam == 'e' or devam == 'E':

   print('Kahve verilerini giriniz: ')
   tanim = input('Tanim: ')

   miktar = int(input('Miktar: '))


   kahve_dos.write(tanim + '\n')
   kahve_dos.write(f'{miktar}\n')

 
   print('Baska bir kayit eklemek isityor musunuz?')
   devam = input('E-e evet: ')
 kahve_dos.close()
 print('Verileriniz kahve dosyasina eklendi.')
KayitEkle() 

 
def KayitAra():
 # flag gorevinde bool degiskeni olusturalim
 bulundu = False
 
 arama = input('Aranacak bir tanim girin: ')
 kahve_dos = open('kahve.txt', 'r')

 tanim = kahve_dos.readline()

 while tanim != '':
   miktar = float(kahve_dos.readline())
   tanim = tanim.rstrip('\n')

 if tanim == arama:
   print(f'Tanim: {tanim}')
   print(f'Miktar: {miktar}')
   print()

   bulundu = True

 tanim = kahve_dos.readline()
 kahve_dos.close()
 if not bulundu:
    print('Bulunamadi.')

KayitAra()
 