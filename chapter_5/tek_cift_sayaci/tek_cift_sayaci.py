import random

cift_sayi=[]
tek_sayi=[]

for number in random.sample(range(1000),100):
    print(number)
    if (number % 2) ==0:
        cift_sayi.append(number)
     
    else:
        tek_sayi.append(number)
               
print('Toplam cift sayi miktari: ' , len(cift_sayi))
print('Toplam Tek sayi miktari: ' , len(tek_sayi))