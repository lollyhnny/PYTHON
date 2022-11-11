
# list ve tuple
# list multiple veri elmani iceren bir nesnedir. dinamik yapidadir
# su sekilde tanimlanir
even_numbers=[2,4,6,8,10]
info=['ogulcan ', 27, 1550.7] #farkli veri tipleri icerebilir.
number= list(range(1,10,2)) #1den 10a kadar 2ser olarak arttir

#tekrarlama operatoru list *n
number1= [0,1,2,3,4]*5
print(number1)

#for dongusu ile bir list uzerinde yineleme
sayilar=[4,65,69,55,78,66]
for sayi in sayilar:
    print(sayilar)

#indexleme
my_list=[10,20,30,40,50]
print(my_list[0],my_list[2])
index=0
while index<5:
    print(my_list[index])
    index+=1

# negatif index kullanimi:
print(my_list[-5],my_list[-1]) # -1. index listenin en sonundaki elemandir

#len fonksiyonu
#dizinin uzunlugunu dondurur

liste=[1,2,3,4,5,67,3,3,36,7]
index=0
while index<len(liste):
    print(liste[index])
    index+=1

#Bir Liste uzerinde Dizine Gore Yinelemek icin for Dongusu Kullanma
names=['birsen','ogulcan','buse','beyza','belinay']
for index in range(len(names)):
    print(names[index])

# list ler degistirilebilir dinamik yapilidir
sayi=[78,89,85,65]
print(sayi)
sayi[0]=54
print(sayi)

# listeleri birbirine ekleme
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1 += list2

# list lerde slice kullanimi
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(numbers) 

print(numbers[1:8:2]) # output [2,4,,6,8]

# list teki elementleri in operatoru ile bulma
# item in list 

def main():
    urun_num=['456','778','457','965']
    arama= input('Bir urun numarasi giriniz: ')
    if arama in urun_num:
        print('aradiginiz urun numarasi listede yer aliyor.')
    else:
        print('aradiginiz urun numarasi listede yer almiyor.')
main()

# list metotlari
# append(item) list in sonuna eleman ekler
#index(item) degeri item a esit olan ilk elemanin degerini dondurur.
# insert(index,item) ozel indexe gore eleman ekler
# sort() en dusuk degerden en yuksek degere kadar listedeki ogeleri artan duzende siralar
# remove(item) 
# reverse() listedeki ogelerin sirasini ters cevirir

name_list=['birsen','buse','ogulcan']
name=input('Eklemek istediginiz ismi giriniz: ')
name_list.append(name)
print('baska bir isim ekleyiniz')


name1=input(' isim: ')
name_list.append(name1)

print()

print('yeni listeniz: ')
print(name_list)

name_list.insert(2,'beyza')
print(name_list)
name_list.sort()
print('listenin ters cevrilmis hali: ')
print(name_list)
name_list.remove('buse')
print(name_list)

# del kullanimi
list=[1,5,6,8]
print(f'liste: {list}')
del list[2]
print(f'silinmis liste: {list} ')

#min ve max foksiyonlari
my_list = [5, 4, 3, 2, 50, 40, 30]
print('The lowest value is', min(my_list))
print('The highest value is', max(my_list))

#list leri kopyalama
list1 = [1, 2, 3, 4]
list2 = list1
#veya
list1 = [1, 2, 3, 4,5]
list2=[]
for item in list1:
    list2.append(item)

    # bir fonksiyondan bir list dondurme

def main1():

 numbers = get_values()


 print('The numbers in the list are:')
 print(numbers)

def get_values():

  values = []

  again = 'y'

  while again == 'y':
    num = int(input('Enter a number: '))
    values.append(num)

    print('Do you want to add another number?')
    again = input('y = yes, anything else = no: ')
    print()

  return values

main1()

# list elemanlarini rastgele secme
import random 
names=['jenny','kelly','chloe','John']
winner=random.choice(names)
print(winner)
