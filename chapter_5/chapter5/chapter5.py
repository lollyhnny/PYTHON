#chapter5
#fonksiyonlar: belirli bir gorevi gerceklestirmek amaciyla bir program icinde bulunan bir grup ifadedir.
# void fonk , icerdigi ifadeleri yurutur ve ardindan sonlandirir
#deger donduren fonk, icerdigi ifadeleri yurutur ve  ardindan onu cagiran ifadeye bir deger dondurur. 
#fonksiyon isimlendirmede degisken isimlendirmede kullanilan kurallar kullanilir.

#pythonda genel bir fonksiyon tanimlama formati:
#def function_name():
#statement
#statement
#etc

def message():
    print('I am Arthur')
    print('King of the Britons.')


def main():
    print('I have a message for you  ')
    message()
    print('Goodbye')

main() #fonksiyonu tanimladiktan sonra cagirmaliyiz.

#pass keyword
x=40
y=56
if x > y:
 pass
else:
 pass

#yerel degiskenler: fonskiyonun icinde olusturulur ve fonksiyonlar birbirlerinin yerel degiskenlerine erisemez
#bundan dolayi farkli fonksiyonlar ayni isme sahip yerel degiskenler kullanabilir
def start():
    texas()
    california()

def texas():
    birds=5000
    print(f'Texas has {birds} birds')
def california():
    birds=8000
    print(f'California has {birds} birds.') #ayni isimde 2 farkli yerel degisken kullandik.

start()

#parametre kullanimi
def show_double(number):
 result = number * 2
 print(result)
show_double(56) #fonksiyona spesifik bir parametre atadik
#
def main1():
    print('12 ve 45\'in toplami:  ')
    toplam(12,45)

def toplam(a,b):
    toplam= a + b
    print(toplam)
main1()
#
def main2():
    first_name= input('Isminizi giriniz: ')
    last_name= input('Soyisminizi giriniz: ')
    print('Isminizin ters cevrilmis hali: ')
    reverse_name(first_name,last_name)

def reverse_name(first,last):
    print(last,first)

main2()
#Global degiskenler ve Global Constants(Sabitler)
#Bir program dosyasindaki tum fonksiyonlar global degiskene erisebilir
my_value=56
def show_value():
    print(my_value)
def kare_al():
    kare=my_value*my_value
    print('kare: ',kare)

show_value()
kare_al()

#global constants
CONTRIBUTION_RATE = 0.05 #global const

def main3():
 gross_pay = float(input('Enter the gross pay: '))
 bonus = float(input('Enter the amount of bonuses: '))
 show_pay_contrib(gross_pay)
 show_bonus_contrib(bonus)


def show_pay_contrib(gross):
 contrib = gross * CONTRIBUTION_RATE
 print(f'Contribution for gross pay: ${contrib:,.2f}.')

def show_bonus_contrib(bonus):
 contrib = bonus * CONTRIBUTION_RATE
 print(f'Contribution for bonuses: ${contrib:,.2f}.')

main3()

