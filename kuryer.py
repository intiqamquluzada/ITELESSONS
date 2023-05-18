# class Sifaris:
#     def __init__(self, id, gonderen, alici, address):
#         self.id = id
#         self.gonderen = gonderen
#         self.alici = alici
#         self.address = address
#         self.status = "Davam eden"
#
#     def get_status(self):
#         return self.status
#
#     def set_status(self, status):
#         self.status = status
#
#
# class Catdirilma:
#     def __init__(self, kuryer, sifaris):
#         self.kuryer = kuryer
#         self.sifaris = sifaris
#         self.status = "Davam eden"
#
#     def get_status(self):
#         return self.status
#
#     def set_status(self, status):
#         self.status = status
#
#
# class Kuryer:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.deliveries = []
#
#     def add_delivery(self, delivery):
#         self.deliveries.append(delivery)
#
#     def get_deliveries(self):
#         return self.deliveries
#
#
# class CatdirilmaSistemi:
#     def __init__(self):
#         self.packages = []
#         self.couriers = []
#
#     def add_package(self, package):
#         self.packages.append(package)
#
#     def add_courier(self, courier):
#         self.couriers.append(courier)
#
#     def get_packages(self):
#         return self.packages
#
#     def get_couriers(self):
#         return self.couriers
#
#     def assign_delivery(self, courier, package):
#         delivery = Catdirilma(courier, package)
#         courier.add_delivery(delivery)
#         package.set_status("Yolda")
#         delivery.set_status("Yolda")
#
#     def complete_delivery(self, delivery):
#         delivery.set_status("Catdirildi")
#         delivery.package.set_status("Catdirildi")
#
# print(555)


# class Avtomobil:
#     def __init__(self, marka, model, reng, gunluk_qiymet):
#         self.marka = marka
#         self.model = model
#         self.reng = reng
#         self.gunluk_qiymet = gunluk_qiymet
#         self.kirayede = False
#
#     def kirayele(self):
#         if not self.kirayede:
#             self.kirayede = True
#             print("Masin kirayelendi.")
#         else:
#             print("Masin onsuzda kirayelenib.")
#
#     def geri_qaytarildi(self):
#         if self.kirayede:
#             self.kirayede = False
#             print("Masin geri qaytarildi.")
#         else:
#             print("Masin onsuzda qaytarilib.")
#
#     def __str__(self):
#         return f"{self.marka} {self.model} ({self.reng}) - Gunluk qiymet: {self.gunluk_qiymet}"
#
#
# class AvtomobilIcareSistemi:
#     def __init__(self):
#         self.masinlar = []
#
#     def masin_elave_et(self, masin):
#         self.masinlar.append(masin)
#
#     def masin_kirayele(self, marka, model):
#         for masin in self.masinlar:
#             if masin.marka == marka and masin.model == model:
#                 masin.kirayele()
#                 return
#         print("Istediyiniz masin tapilmadi.")
#
#     def masini_geri_qaytar(self, marka, model):
#         for masin in self.masinlar:
#             if masin.marka == marka and masin.model == model:
#                 masin.geri_qaytarildi()
#                 return
#         print("İstediyiniz masin tapilmadi")
#
#     def masinlari_goster(self):
#         if len(self.masinlar) > 0:
#             print("Movcud avtomobiller:")
#             for masin in self.masinlar:
#                 print(masin)
#         else:
#             print("Movcud avtomobil yoxdur.")
#
#
# # Bezi masin obyektleri yaradaq burada
# masin1 = Avtomobil("Audi", "A5", "Boz", 200)
# masin2 = Avtomobil("BMW", "X5", "Qara", 300)
# masin3 = Avtomobil("Mercedes", "E200", "Ag", 250)
#
# # Masin kirayeleme sistemini tanidiriq burda
# sistem = AvtomobilIcareSistemi()
#
# # Masinlari sisteme saliriq burada
# sistem.masin_elave_et(masin1)
# sistem.masin_elave_et(masin2)
# sistem.masin_elave_et(masin3)
#
# # Masinlari goster
# sistem.masinlari_goster()
#
# # Bu masinlari icareye goturek
# sistem.masin_kirayele("Audi", "A5")
# sistem.masin_kirayele("Audi", "A5")


# -------------------------------------------------------------------

x = [['Yanvar', 15, 18],
     ['Fevral', 12, 20],
     ['Mart', 13, 18],
     ['aprel', 18, 18],
     ['may', 21, 15],
     ['iyun', 13, 18],
     ['iyul', 14, 18],
     ['avqust', 12, 18],
     ['sentyabr', 16, 25],
     ['oktyabr', 22, 23],
     ['noyabr', 10, 15],
     ['dekabr', 15, 18]]

# 1.
# for lst in x:
#     print(lst[1])  # alis qiymetleri

# 2.
maksimum = 0
for lst in x:
    if lst[2] > maksimum:
        maksimum = lst[2]
print(maksimum)

# 3.

alis = []
satis = []
for lst in x:
    alis.append(lst[1])
    satis.append(lst[2])

minimum_alis = min(alis)
maksimum_satis = max(satis)
for i in x:
     if i[1] == minimum_alis:
          minimum_alis_ay = i[0]
     if i[2] == maksimum_satis:
          maksimum_satis_ay = i[0]
print(minimum_alis_ay, maksimum_satis_ay)