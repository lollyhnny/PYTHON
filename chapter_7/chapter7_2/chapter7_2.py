# LIST VE DOsYALAR ILE CALISMA
# dosyadaki degerleri siralamanin bir teknigi bunlari bir liste halinde okumak listenin siralama yontemini cagirmak ve ardindan listedeki degerleri dosyaya geri yazmaktir
# python dosya nesnelerinin tum listeyi bir dosyaya yazan 'writelines isimli bir yontemi vardir bu yontemin dezavataji her ogenin sonuna otomatik olarak yeni bir satir ('\n) yazmamasidir.
#sonuc olarak bu yontem her ogeyi dosyadaki uzun bir satira yazar.

def main():
    sehirler=['Ankara ','Istanbul','Denizli','Sivas']
    dos=open('sehirler.txt','w')
    for item in sehirler:
        dos.write(item+'\n')
    dos.close()

    #burada bir dosyanin icerigini bir liste halinde okuyacagiz.
    dos1=open('sehirler.txt','r') 
    sehirler=dos1.readlines()
    dos1.close()
    for index in range(len(sehirler)):
        sehirler[index]= sehirler[index].rstrip('\n')
    print(sehirler)
main()
# f-string kullanarak da bir dosyaya yazma islemi yapabiliriz
# burada dos_degiskeni.write(f'{item}\n') kullanabiliriz
def main1():
    sayilar=[44,55,11,77,88,89,64,14]
    dos=open('sayilar.txt','w')
    for item in sayilar:
        dos.write(str(item)+'\n')
    dos.close()
    dos1=open('sayilar.txt','r')
    sayilar=dos1.readlines()
    dos1.close()
    for index in range(len(sayilar)):
        sayilar[index]=int(sayilar[index])
    print(sayilar)
main1()

####
# Mevcut bir listenin ogelerini yineleyerek yeni bir liste olusturma

list1=[1,2,3,4]
list2=[]
for item in list1:
    list2.append(item)
print(list2)
#veya
list3=[1,2,7,8,9]
list4=[item for item in list3]
list5=[item**2 for item in list3] # list3 deki elemanlarin karesini alarak list5 e ekler
print(list4)
print(list5)

#if kullanimi ile ayni islemi yapalim
list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = []
for n in list1:
  if n < 10:
    list2.append(n)
print(list2)

#len kullanimi
last_names = ['Jackson', 'Smith', 'Hildebrandt', 'Jones']
short_names = [name for name in last_names if len(name) < 6]
print(short_names)

####

#iki boyutlu liste tanimlama:
def main3():
    import random
    values=[[1,2,3],
            [10,20,30],
            [100,200,300]]
    for satir in values:
        for element in satir:
            print(element) #dunyanin en sacma kodu

#random deger atalim

    satir=3
    sutun=3
    for x in range(satir):
        for y in range(sutun):
            values[x][y] = random.randint(1, 100)
    print(values)
       
main3()