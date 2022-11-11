import pickle
dos=open('bilgiler.dat','wb')
veriler={'isimler':' ','kilo':'0','boy':'0'}
devam ='e'
while devam== 'e' or devam == 'E':
    veriler['isimler']=input('Isim: ')
    veriler['kilo']=input('Kilo: ')
    veriler['boy']=input('Boy: ')
    pickle.dump(veriler,dos)
    devam=input('Yeni veri eklemek istiyor musunuz? (Evet icin e-E giriniz): ')
dos.close()
dos=open('bilgilerBirsen.dat','rb')
dosya_sonu = False
while not dosya_sonu:
    try:
        veriler=pickle.load(dos)
        print('Isim: ' + veriler['isimler'])
        print('Kilo: ' + veriler['kilo'])
        print('Boy: ' + veriler['boy'])
    except EOFError:
        dosya_sonu=True
dos.close()