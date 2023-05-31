# 1.Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin.
# cumle = input("Cumleni daxil edin: ")
# cumle_list = cumle.split()
# string = ""
# for i in cumle_list:
#     soz = "".join(sorted(i))
#     string = string + soz + " "
#
# print(string)

# mylst = ['salam', 'salam2']
# print(str(mylst))
# mylst = ['s', 'a', 'l']
# soz = "-".join(mylst)
# print(soz)


# Eger eyni ad soyad tekrar olarsa, meselen: intiqam.quluzade@trainer.edu.az,
# ikinci defe olduguna gore intiqam.quluzade2@trainer.edu.az olacaq.
# Ve ad soyadlar bele balacaldilmis sekilde olmalidir.


# siyahi = ['Intiqam Quluzade', 'Etibar Vezirov', 'Vali Aliyev', 'Iltifat Quliyev',
#           'Fateh Quliyev', 'Intiqam Quluzade',
#           'Intiqam Quluzade', 'Fateh Quliyev']
#
# qelib = "@trainer.edu.az"
#
# details_list = []
# bos_list = []
# for i in siyahi:
#     email_user = ".".join(i.lower().split())
#     bos_list.append(email_user)
#     if bos_list.count(email_user) > 1:
#         email_user += f"{bos_list.count(email_user)}"
#     email_user += qelib
#     details_list.append(email_user)
#
#     email_user = ""
#
# print(details_list)

# ---------------------------------------------------

#
# 3.# 1   0   1   0
#   # 0   1   0   1
#   # 1   0   1   0
#   # 0   1   0   1
# a = [
#     [1,0,1,0],
#     [0,1,0,1],
#     [1,0,1,0]
# ]

# setir = int(input("Setir sayini daxil edin: "))
# sutun = int(input("Sutun sayini daxil edin: "))
#
#
# matris = []
#
#
# for i in range(setir):
#     sira = []
#     for j in range(sutun):
#         sira.append(0)
#     matris.append(sira)
#
#
# print(matris)
#
# for i in range(setir):
#     for j in range(sutun):
#         if i == j:
#             matris[i][j] = 1
#
#
# for i in matris:
#     print(i)

# ------------------------------------------------


# def divider(lst, num):
#     new_list = []
#     for i in lst:
#         try:
#             new_list.append(i % num)
#         except Exception as e:
#             continue
#     return new_list
#
#
# print(divider([2, 3, 4, 2, 's', 5, 3], 2))


# 2. String olaraq ixtiyari sayda daxil edilen tam ededleri integer tipine cevirib onlarin harmonik
#    ortasinin hesablayib qaytaran funksiya yazin.


# def harmonic_mean(*args):
#     sum = 0
#     uzunluq = 0
#     for i in args:
#         try:
#             sum += (1 / int(i))
#             uzunluq += 1
#
#         except Exception as e:
#
#             continue
#         return uzunluq / sum
#
#
# print(harmonic_mean('3', '4', '2', 's'))


























