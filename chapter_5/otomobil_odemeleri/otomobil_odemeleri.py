 
kredi_odemesi=float(input('Mevcut Kredi odemenizi giriniz: '))
sigorta_odemesi=float(input('Mevcut Sigorta odemenizi giriniz: '))
benzin_odemesi=float(input('Mevcut benzin odemenizi giriniz: '))
akaryakit_odemesi=float(input('Mevcut benzin odemenizi giriniz: '))
lastik_odemesi=float(input('Mevcut lastik odemenizi giriniz: '))
bakim_odemesi=float(input('Mevcut bakim odemenizi giriniz: '))
toplam_tutar=kredi_odemesi + sigorta_odemesi + benzin_odemesi + akaryakit_odemesi + lastik_odemesi + bakim_odemesi 
print (f'Aylik yoplam odeme tutariniz: {toplam_tutar}')

def YillikOdemeGoster():
    yillik_odeme= toplam_tutar *12
    return yillik_odeme
    

print(f'Yillik toplam odeme tutariniz: {YillikOdemeGoster()} ')

