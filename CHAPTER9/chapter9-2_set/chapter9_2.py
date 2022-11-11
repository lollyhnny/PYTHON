#SET(KUME)
# bir kume benzersiz degerler koleksiyonu icerir ve matematiksel bir kume gibi calisir

#Bir kume yaratma
myset= set() # burada bos bir kume olusturuyoruz
myset=set(['a','b','c'])
# set fonksiyonuna bir dize iletirsek dizedeki her bir karakter kumenin bir uyesi olur 
myset1=set('abc')
print(myset1)
myset2= set('aaabbbbccc')
print(myset2)
myset3 = set('one two three')
# bu kumeyi myset3 = set('one', 'two', 'three') seklinde tanmlayamayiz
#fakat myset3 = set(['one', 'two', 'three']) bu sekilde tanimlayabilriz
print(myset3)

#eleman ekleme caldirma
myset4 = set()
myset4.add(1)
myset4.add(2)
myset4.update([3,4, 5, 6])
myset4.remove(1)
print(myset4)

#kumelerin birlesimini bulma
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6]) 
set3 = set1.union(set2)
print(set3)

#Kumelerin kesisimini bulma
set4=set1.intersection(set2)
print(set4)