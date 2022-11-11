def main():
    dos = open("kaynak.txt", "r")
    satirlar = {}
    satir_num = 1

    for satir in dos.readlines():
        satir = satir.strip().split(' ')
        for kelime in satir:
            if kelime not in satirlar.keys():
                satirlar[kelime] = str(satir_num)
            else:
                satirlar[kelime] = satirlar[kelime] + " " + str(satir_num)
        satir_num = satir_num + 1
    dos.close()
    dos1=open('analiz.txt','w')
    for key in satirlar.keys():
        dos1.write(key + " : " + satirlar[key] + "\n")
    dos1.close()
main()