#chapter 3



test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))
ortalama = (test1 + test2 + test3) / 3
print(f'Ortalamaniz: {ortalama} ')
if ortalama>=50:
   print("Dersten gectiniz.")
else:
   print("Dersten kaldiniz.")


#string karsilastirma
#1
sifre = input('Sifrenizi giriniz: ')
sifre1='slimshady'

if sifre == sifre1:
   print('sifre kabul edildi')
else:
   print('yanlis sifre')

#2
isim1=input('1.ismi giriniz:')
isim2=input('2.ismi giriniz:')
if isim1 > isim2:
    print(f'{isim1} {isim2} den daha onde ')
else:   
    print(f'{isim2} {isim1} den daha onde')

    #karar yapilari
score=int(input('Enter the score'))
if score>50:
    print('score C')
elif score>70:
    print('score B')
elif score>80:
    print('score A')
else:
   print('kaldiniz')

#truth table 
#and operator
#true and false false
#false and true false
#false and false false
#true and true true

#or operator
#true or false true
#false or true true
#false or false false
#true or true true

x=30
if x>20 or x<40:
  print('deger kabul edilen aralikta')

#
sales=int(input('indirim miktarini giriniz: '))
if sales >= 500.0:
 indirimkotasi = True
else:
 indirimkotasi = False

if indirimkotasi==True:  
   print('indirim kotaniz dolmustur...')


