#chapter4
#donguler


#for loop (count controlled loop)
print('I will display the numbers 1 through 5.')
for num in [1, 2, 3, 4, 5]:
  print(num)

for name in ['Winken', 'Blinken', 'Nod']:
  print(name)

#range kullanimi(sinir koyma)
for nums in range(1, 30, 2 ):
  print(nums)

#
print('Number\tSquare')
print('--------------')

for number in range(1, 11):
  square = number**2
  print(f'{number}\t{square}')

#ic ice gecmis donguler
for hours in range(24):
  for minutes in range(60):
    for seconds in range(60):
      print(hours, ':', minutes, ':', seconds)

#
satir=int(input('satir sayisi: '))
sutun=int(input('sutun sayisi: '))
for x in range(satir):
  for y in range(sutun):
    print('*',end=' ')
  print()   

#while loop kosul dogru oldugu surece devam eder.
keep_going = 'e' or 'E'
 
while keep_going == 'e' or 'E':

  indirim = float(input('indirim miktarini giriniz: '))
  komisyon_orani = float(input('komisyon oranini giriniz: '))
  komisyon = indirim * komisyon_orani
  print(f'Komisyon ${komisyon:,.2f}.')

  keep_going = input('Baska hesaplama yapmak istiyor musunuz?  ' +
'komisyon (evet icin e veya E giriniz): ') #sonsuz dongu
