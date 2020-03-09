

agirlik = int (input("Lütfen ağırlığınızı giriniz(kg):"))
boy = int (input("Lütfen boyunuzu giriniz (cm):"))

boy = boy/100.0
bki = agirlik/(boy*boy)

print("BKİ".format(round(bki)))

print ("BKİ: ", bki)


if  bki < 18.5 :

    print("Zayıfsınız")

    print("3 kg Almanız Gerekiyor".format(round(25*(boy*boy) - agirlik)))

elif bki< 25 :

    print("Normal Kilodasınız")

elif bki < 30:

    print("Fazla Kilolusunuz")

    print("5 kg Vermeniz Gerekiyor".format(agirlik - round(25*(boy*boy) )))

elif bki < 35:

    print("1. Derece Obezsiniz")

    print("8 kg Vermeniz Gerekiyor".format(agirlik - round(25*(boy*boy) )))

elif bki < 40:

    print("2. Derece Obezsiniz")

    print("10 kg Vermeniz Gerekiyor".format(agirlik - round(25*(boy*boy) )))

elif bki < 45:

    print("3. Derece Obezsiniz")

    print("15 kg Vermeniz Gerekiyor".format(agirlik - round(25*(boy*boy) )))
