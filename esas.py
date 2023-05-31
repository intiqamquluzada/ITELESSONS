from cylinder import tam_s, yan_s, hecm, oturacaq_s

print(tam_s(5, 6))
say = int(input("Isci sayi: "))

with open("employee.txt", "w") as fayl:
    for i in range(say):
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        ata_adi = input("Ata adi: ")
        email = input("Email: ")

        fayl.write(f"{ad},{soyad},{ata_adi},{email}\n")

mylst = []

with open("employee.txt", "r") as fayl:
    for setir in fayl:
        ad = setir.split(",")[0]
        soyad = setir.split(",")[1]
        ata_adi = setir.split(",")[2]
        email = setir.split(",")[3]

        mylst.append(ata_adi)

print(mylst)

