#TUPLES
# Tuple icerigi degistirilemez bir dizidir () kullaniriz listelerle ayni sekilde tum operasyonlari destekler
my_tuple=(1,2,3,4,5)
print(my_tuple)

#listeler ve tuple lar arasinda donusturme
# bir tuple i listeye dondustumek icin list() fonksiyonunu kullaniriz ayni sekilde bir listeyi tuple a donusturmek icin de tuple() fonksiyonunu kullaniriz.

number_tuple=(1,2,3)
number_list=list(number_tuple)
print(number_list)
str_list=['one','two','three']
str_tuple=tuple(str_list)
print(str_tuple)