#Dictionary(Sozluk)
#  bir veri koleksiyonu depolayan nesnedir. 
#  sozlukteki her ogenin iki bolumu vardir: Bir key ve bir value 
#  belirli bir degeri bulmak icin key kullaniriz.
# bir sozluk {} ile tanimlanir
# keyler ve value lar buyuk kucuk harfe duyarlidir

tel_defteri={'Buse':'4565','Beyza':'5623','Ogulcan':'1003','Belinay':'8956'}
#burada 1. elemenler key 2. elementler value degerleridir

#sozlukten deger almak 
tel_defteri['Buse']

# bir sozlukte bir degeri test etmek icin in ve not in kullanma
if 'Ogulcan'in tel_defteri:
    print(tel_defteri['Ogulcan'])
if 'Sude' not in tel_defteri:
    print(' Sude  bulunamadi..')

#Var olan bir sozluge eleman ekleme dictionary_name[key]=value
tel_defteri['Sude']='5687'
print(tel_defteri['Sude'])
# NOT: bir sozlukte ayni keyleri kullanamayiz mevcut bir anahtara bir deger atadigimizda yeni deger mevcut olan degerin yerini alir.

#silme islemi:
del tel_defteri['Sude']
print(tel_defteri)

#Bir sozlukte veri turlerini karistirma
sozluk={'Kayla':[88,99,100],'Sophie':[66,77,85]} # burada value degerleri bir list aliyor

sozluk1={'Key1':[1,2,8],'Key2':'Hollanda','Key3':5,'Key4':(7,9,11),('Key4'):(7,5,1)} #tek bir sozlukte saklanan degerler farkli turlerde olabilir
print(sozluk1)

#Bos bir sozluk yaratma
phonebook={}
phonebook['chris']='555-111'
phonebook['Sophie']='125-111' # bos sozluge key ve degrleri ekliyoruz
print(phonebook)

# bos bir sozluk olusturmak icin dictionary_name=dict() methodunu da kullanabiliriz.
name=dict()
name['isim1']='Ogulcan'
name['isim2']='Birsen'
print(name)

#BAZI SOZLUK METHOTLARI
#clear > Bir sozlugun icerigini temizler
#get > Belirtilen anahtarla iliskili degeri alir
#items > Bir sozlukteki tum anahtarlari ve bunlarla iliskili degerleri bir tuple olarak dondurur
#keys > Bir sozlukteki tum anahtarlari bir tuple olarak dondurur
#values > Bir sozlukteki tum  degerleri bir tuple olarak dondurur
#pop > Belirtilen bir anahtarla iliskili degeri dondurur ve bu anahtar/deger ciftini sozlukten kaldirir

phonebook2 = {'Chris':'555−1111', 'Katie':'555−2222'}
value = phonebook.get('Katie', 'Entry not found')
print(value)

for key in phonebook.keys():
    print(key)

# sozluk tanımlamada if kullanimi
populations = {'New York': 8398748, 'Los Angeles': 3990456, 
 'Chicago': 2705994,'Houston': 2325502, 
 'Phoenix': 1660272, 'Philadelphia': 1584138}
largest = {}
for k, v in populations.items():
  if v > 2000000:
   largest[k] = v
print(largest)

