#chapter 2
#output 
from base64 import b16decode, b16encode
from dataclasses import dataclass
from stringprep import b1_set


print("Kate austen")
print('Kate austen')
print("""Kate austen""")

#variables
room=127
print("i am staying in room number")
print(room)

#input
isim = input('isminiz: ')
soyisim = input('soyisminiz: ')
print('Hosgeldniz', isim, soyisim)

#veri donusumu
#int(item) float(item)

value=int(input('How many hours did you work?'))

#float integer division
a=5
b=2
result=a/b
print(result) #float
c=5
d=2
result2=c//d
print(result2) #float

# end=' '
print('one',end=' ')
#sep=''
print('one',"two","three",sep='*')

#escape characters
#\n new line
#\t Causes output to skip over to the next horizontal tab position.
#\' Causes a single quote mark to be printed.
#\" Causes a double quote mark to be printed.
#\\ Causes a backslash character to be printed.

#formating strings
name='birsen'
print(f'hello  {name}')
pi = 3.1415926535
print(f'{pi:.3f}')

number = 123456
print(f'{number:,d}') 
 #sutun column 
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999
print(f'{num1:10.2f}{num2:10.2f}') 
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')

#hizalama
name2 = 'Jay'
print(f'Hello {name2:10}. Nice to meet you.')
