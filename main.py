# phrase = ['biz', 'print', 'funksiyasina', 'baxiriq', 've', 'tetbiq', 'edirik']
#
#
# for word in phrase:
#     print(word, end=' ')
# print()
# print()
# print('salam', 'Intigam', sep='-')
# print(555)


# a = 'salam'
# print('hi {} {}'.format(a,a))


# a = 2 / 3
# print(round(a, 3))


# a = 1 + 4j
# print(type(a))


# a = 4
# print(complex(a))

# a = -3
# print(complex(a))

# a = 4.5
# print(complex(a))

# a = 5.234547
# print(round(a, 4))


# i = range(6)
# print(i)

# for i in range(5):
#
#     if i == 3:
#         break
#     print(i)

# a = "Hello, Horld!"
# print(a.replace("H", "J"))

#
# a = 'salam, yoldaslar'
# b = a.split(',')
# print(b)
# print(a.capitalize())


#     PYTHON INNOVATIV TEXNOLOGiYALAR MERKEZI


# -----------------------------------------------------------------------------------
# 2*3 = 6
# 3*3 = 9
# 4*3 = 12
# 5*3 = 15
# 6*3 = 18
# 7*3 = 21
# 8*3 = 24
# 9*3 = 27


# print('\n'.join([f'{i}*3 = {i * 3}' for i in range(2, 10)]))

# ------------------------------------------------------------------------------------


# a = '9'
# b = '10'
# print(a > b)
# bu kodun neticesi true-dir Bu ona gore bize True qaytarir ki, bunlar string tipindedirler ve bunlari
# sirf ASCII deyerlerine gore muqayise ede bilir. Yeni bunlar eded kimi muqayise olunmur,
# ASCII deyerlerine gore de muqayise edende soldan birinci reqemle muqayise edirik, hansinin ASCII deyeri
# boyukduse o boyuk olur, yox eger ilk reqemler eyni olarsa sonraki reqemlerin ASCII deyerlerine gore
# muqayise olunur. 3 reqemli ile 2 reqemlini muqayise elemek istedikde ise 1ci iel 1-ci 2-ci ile 2ci
# 3-cu ile yene 2ci muqayise olunur. Yalnizca bu sertler odendikde true qaytarir bele olan halda: <<<, >>>
# basqa hallarda false qaytarir


# ---------------------------------------------------------------------------------------


# def outer(a):
#     b = 10
#
#     def inner(c):
#         d = 11
#         return a * b + c * d
#
#     return inner(5)
#
#
# print(outer(4))

"""
burada funksiya daxilinde funksiya cagirilmisdir (callback function). outer funksiyasina daxil olur ve onun daxiline
4 deyerini gonderir, bu zaman outer funksiyasi ise dusur ve b = 10 menimsederek kecir daxilinde olan inner 
funksiyasina. Inner funskiyasi da bize a*b+c*d qaytardigina gore yerine qoyuruq ve aldigimiz netice 95 olur.
Burada qlobal deyisenler yoxdur. Butun deyisenler lokaldir. a ve b deyiseni outer funskiyasinin lokal deyiseni,
c ve d ise inner funksiyasinin lokal deyisenidir. Eger bu deyisenlerden her hansi birini global etmek istese idik,
qarsisina global yazmagimiz kifayet idi. vE BU ZAMAN DEYERINI FUNKSIYANIN ICINDEN DEYIL YUXARIDA ELAN
OLUNDUGU YERDEKI DEYERDEN GOTURECEKDI.
"""
import random

# ---------------------------------------------------------------------------

"""
Istifadəçidən x və y dəyişənləri vasitəsilə götürülən həqiqi ədədlərin ən kiçiyini
 almaq üçün pythonkodu yazın,
 belə ki if-else operatorları və min() funksiyası istifadə edilməməlidir. 
 Yalnız müqayisə və cəbri operatorlar istifadə oluna bilər.
"""

# x = float(input("x-i daxil edin: "))
# y = float(input("y-i daxil edin: "))
#
# minimum = x * (x < y) + y * (y < x)
#
# print(minimum)


"""
burada mesele ondan ibaretdir ki, x<=y ve y<x bize sadece True yaxud False deyerlerini elde etmke ucun lazimdir
Bildiyimiz kimi True  = 1 , False= 0. buradada eger x <= y olarsa (x<=y) = 1 olur ve ikinci sert avtomatik 
olaraq false olduguna gore sifir olur ve sifirlanir, umumi neticemiz yeni minimum deyerimiz beraber olur
x * 1 -e. Diger halda da sol teref false qaytarir sag teref true ve y*1 olur.  
"""

# ----------------------------------------------------------------------
# a = [1, 2, 3, 4]
# b = [50, 100]
# b[1] = 100
# print(a)

"""
burada minimum 2 elementli ve 1-ci indeksinde 100  olan istenilen list yazila biler. Ve eks halda error
cixacagina gore cap etmeyecek.
"""
# --------------------------------------------------------------------------
"""

Təksətrli if-else operatoru istifadə etməklə (ternary) istifadəçidən alınan 
x,y və z həqiqi ədədlərinin 
ən böyüyünü tapıb çap edən Python kodu yazın (min() funksiyası istifadə etmədən).

"""
# x = float(input("x-i daxil edin: "))
# y = float(input("y-i  daxil edin: "))
# z = float(input("z-i daxil edin: "))
# print(x if x > y and x > z else y if y > z else z)


"""
burada x capa verilecek nevaxt - eger x hem y-den hemde z-den boyuk olarsa, 
eger if serti odenmezse avtomatik olaraq else halina kecirik
yoxlayiriq y > z-den boyukdurse y-i capa verir burda daha y > x yoxlamiriq cunki artiq emeliyyat lazim deyil
onsuzda if sertinde yoxlamisiq bunu. Ve nehayet y>z  sertide odenmezse avtomatik olaraq kecir 
son else halina ve z-i cap edir

"""

# --------------------------------------------------------------------------


# with open('A.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
#

# encoding='utf-8' parametri bize imkan verir ki, tekce ASCII cedvelinde olan simvollarla deyil xususi
# simvollarla da isleye bilek. Azerbaycan elifbasi da bura aiddir.


# -------------------------------------------------------------------------------


# funksiya = lambda eded: 0 if eded == 0 else (eded % 10) + funksiya(eded // 10)

"""
burada eded bizim parametrimizdi. eger eded = 0 olarsa cavab olaraq 0 qaytarilacaq. eks halda
rekursiya teskil olunacaq ve sert yeni qirilma noqtesi funksiya(0) olana qeder gedecek. Yeniden yerine
qoya-qoya ededin reqemlerinin cemi tapilacaq
"""

# -----------------------------------------------------------------------------------

# Yuxarıda verilmiş iki kəsrin cəmini hesablayan funksiyanı tamamlayın.
# Parametrdən göründüyü kimi kəsrlər a və b parametrləri vasitəsilə tuple tipində götürülür.
# Əgər funksiyaya heç bir parametr verilməzsə bu zaman 3/4 + 4/5 cəmini hesablayacaq.
# a və b kəsrlərinin surətləri uyğun olaraq a[0] və b[0],
# məxrəcləri isə uyğun olaraq a[1] və b[1] dəyərləridir.
# Funksiyadan nəticə olaraq cavab kəsr şəklində (string formatında) qaytarılmalıdır.

# def kesrlerin_cemi(a=(3, 4), b=(4, 5)):
#     suret = a[0] * b[1] + b[0] * a[1]
#     mexrec = a[1] * b[1]
#     netice = f"{suret}/{mexrec}"
#     return netice
#
#
# print(kesrlerin_cemi((2, 9),(3, 4)))

"""
adi kesrlerin toplanmasi qaydasindan istifade edirik
"""
# ---------------------------------------------------------------------------------------

# a və b tam ədədləri üçün a üstü b qüvvətini rekursiv üsulla hesablayan funksiya yazın


# def quvvet(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * quvvet(a, b - 1)
#
#
# print(quvvet(3, 4))
"""
burada eger quvvet sifir olarsa musbet ededin ustu sifir olanda 1 alindigini bilirik ve 1-i geri dondururuk
eks halda ise rekursiya basladiriq ve her defe devam edir o vaxta qeder ki, return 1 alacaq. Sonra yeniden 
geri qayidir ve yerine qoya qoya gonderilen parametrlere uygun hesablayir

"""

# ------------------------------------------------------------------


# num = int(input("Rəqəmi daxil edin: "))
#
# count = 0
# for i in range(1, 101):
#     if str(num) in str(i):
#         count += 1
# print(count)


# cumle = input("Cümlə daxil edin: ")
#
# # Cümləni sözlərə bölürük
# sozler = cumle.split()
# mystr = ""
# for soz in sozler:
#
#     soz = "".join(sorted(soz))
#     mystr = mystr + soz + " "
#
#
# print(mystr)

# -------------------------------------------------------------------------------

# 1) 1-dən 100-dək ədədlər içində neçə ədəddə istifadəçi tərəfindən daxil edilən rəqəm var?
# eded = int(input("Ededi daxil edin: "))
# saygac = 0
# for i in range(1, 101):
#     if str(eded) in str(i):
#         saygac += 1
# print(saygac)

# 2) 1-dən 100-dək ədədlər içində ümumilikdə istifadəçidən götürülən rəqəm neçə dəfə istifadə olunmuşdur?
# eded = input("Ededi daxil edin: ")
# a = ""
# for i in range(1, 101):
#     a += str(i)
# print(a.count(eded))

# 3) Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin.

# cumle = input("Cumleni daxil edin: ")
# cumle_list = cumle.split()
# string = ""
# for i in cumle_list:
#     soz = "".join(sorted(i))
#     string = string + soz + " "
#
# print(string)

# 4) Verilmiş cümlədə tərsdən yazılışı özü ilə eyni olan (palindromik söz) neçə söz var?
# cumle = input("Cumleni daxil edin: ")
# saygac = 0
# cumle_list = cumle.split()
# for soz in cumle_list:
#     if soz == soz[-1::-1]:
#         saygac += 1
# print(saygac)

# 5) İki zəri 10 dəfə atarkən qoşa düşən halların sayınının düşməyən halların sayına nisbətini hesablayın.

# zer1 = [1, 2, 3, 4, 5, 6]
# zer2 = [1, 2, 3, 4, 5, 6]
#
# qosa = 0
# adi = 0
# a = 10
# while a > 0:
#     for i in zer1:
#         for j in zer2:
#             if i == j:
#                 qosa += 1
#             else:
#                 adi += 1
#     a -= 1
# print(qosa/adi )


# 6) Ad və Soyadlardan ibarət siyahı verilir.Bu siyahını istifadə etməklə ad.soyad@trainer.edu.az maillərini
#    düzəldən Python kodu yazın.

# siyahi = ['Intiqam Quluzade', 'Etibar Vezirov', 'Vali Aliyev', 'Iltifat Quliyev', 'Fateh Quliyev', 'Intiqam Quluzade',
#           'Intiqam Quluzade', 'Fateh Quliyev']
# qelib = "@trainer.edu.az"
# # details = {}
# details_list = []
# bos_list = []
# for i in siyahi:
#     email_user = ".".join(i.lower().split())
#     # details[i] = email_user
#     bos_list.append(email_user)
#     if bos_list.count(email_user) > 1:
#         email_user += f"{bos_list.count(email_user)}"
#     email_user += qelib
#     details_list.append(email_user)
#
#     email_user = ""
# # print(details)
# print(details_list)

# 7) Indi isə 6-cı məsələdə alınan maillər siyahısını götürüb onların əsasında ad və soyadlardan ibarət bir
#    siyahı düzəldin.

# siyahi = ['intiqam.quluzade@trainer.edu.az', 'etibar.vezirov@trainer.edu.az', 'vali.aliyev@trainer.edu.az',
#           'iltifat.quliyev@trainer.edu.az', 'fateh.quliyev@trainer.edu.az']
# ad_soyad = ""
# yeni_siyahi = []
# for i in siyahi:
#     for j in i:
#         if j == "@":
#             break
#         ad_soyad += j
#         ad_list = ad_soyad.split(".")
#         for u in range(len(ad_list)):
#             ad_list[u] = ad_list[u].capitalize()
#         tam_ad = " ".join(ad_list)
#     yeni_siyahi.append(tam_ad)
#     ad_soyad = ""
# print(yeni_siyahi)


# b_array = bytearray(b'Hello World!')
# print(type(b_array))  # bytearray(b'Hello World!')
# b_array[0:5] = b'python'
# print(b_array)
#


# bytes_obj = bytes('string', 'utf-8')
# bytes_obj[0] = 'x'
# print(bytes_obj)
# print(bytes_obj[0])


# sum = 0
# for i in range(10, 100):
#     if i % 2 == 0:
#         continue
#     sum += i
# print(sum)
#
#
# # for i in range(10,100):
# #     if i % 2 != 0:
# #         sum += i
# # print(sum)


# a = [4, 12, 7, 5, 24, 3, 11, 26, 10]
#
# cem = 0
# hasil = 1
#
# for i in a:
#     cem = cem + i
#     if i % 2 == 1:
#         hasil = hasil * i
# print(cem, hasil)


# a = 5
# b = 10
# assert a > b, "a böyükdür b-dən!"


# import numpy as np
#
# matrix = np.array([[3, 2, 1],
#                    [1, 3, 4],
#                    [2, 1, 3]])
# print(np.max(np.min(matrix, axis=1)))

# myfunc = lambda eded, baslangic, son: "solunda" if eded < baslangic else "saginda" if eded > son else "daxilinde"
#
# print(myfunc(5, 4, 7))
# import random
# eded = random.randint(1, 100)
# print(eded)
# cehd = 0
# while True:
#     user_eded = int(input("Daxil et: "))
#     cehd += 1
#     if user_eded == eded:
#         print('tapdiniz')
#         print(cehd)
#         break
#     elif eded < user_eded:
#             print("asagiya dusun")
#     elif eded > user_eded:
#             print("yuxariya qalxin")

# eded = 2
# start = 1
# end = 200
# powers = [1, ]
# k = 1
# for i in range(start + 1, end):
#     power = eded ** k
#     k += 1
#     if power >= start and power <= end:
#         powers.append(power)
# print(powers)

# eded=3
# baslangic=10
# son=250

# num = 55550
# dict = {
#     5: 4,
#     0: 1
# }

# 5) Daxil edilən çoxrəqəmli ədədin hər bir rəqəmini və onun sayını lüğət elementləri kimi bir lüğət daxilində göstərin.
# eded = input("Ededi daxil edin: ")
# mydict = {}
# for reqem in eded:
#     mydict[reqem] = eded.count(reqem)
# print(mydict)


# ------------------
# setir = int(input("Setir sayini daxil edin: "))
# sutun = int(input("Sutun sayini daxil edin: "))
#
# matris = []
#
# for i in range(setir):
#     sira = []
#     for j in range(sutun):
#         sira.append(0)
#     matris.append(sira)
# print(matris)
# saygac=1
# for i in range(setir):
#     for j in range(sutun):
#         matris[i][j] = saygac
#         saygac += 1
# print(matris)
# # for i in range(setir):
# #     for j in range(sutun):
# #         print(matris[i][j], end=" ")
# #     print()
#
# for row in matris:
#     print(row)
# ------------------------------------------

# setir = int(input("Setir sayini daxil edin: "))
# sutun = int(input("Sutun sayini daxil edin: "))
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
# for i in range(setir):
#     for j in range(sutun):
#         if i == j:
#             matris[i][j] = 1
# print(matris)

# -----------------------------------------

# baslangic = int(input("birinci eded: "))
# son = int(input("son: "))
#
# cem = 0
# hasil = 1
# mylist = []
# for i in range(baslangic, son):
#     cem = 0
#     hasil = 1
#     for j in str(i):
#         cem += int(j)
#         hasil *= int(j)
#     print(cem > hasil)
#
#     if cem > hasil:
#         mylist.append(i)
#     print(cem)
#     print(hasil)
#
#
# print(mylist)

# --------------------------------------------------------------------------------------

# 1   2   3   4
# 0   6   7   8
# 0   0  11  12

# setir = int(input("setir sayini daxil edin: "))
# sutun = int(input("sutun sayini daxil edin: "))
#
# yuxari_ucbucaq_matris = []
#
# for i in range(setir):
#     sira = []
#     for j in range(sutun):
#         sira.append(0)
#     yuxari_ucbucaq_matris.append(sira)
# saygac = 1
# for i in range(setir):
#     for j in range(sutun):
#         if i <= j:
#             yuxari_ucbucaq_matris[i][j] = saygac
#         saygac += 1
# #asagi
# for i in range(setir):
#     sira_2 = []
#     for j in range(sutun):
#         sira_2.append(0)
#     asagi_ucbucaq_matris.append(sira_2)
#
# #yuxari
#

#
# #asagi
# saygac_ = 1
# for i in range(setir):
#     for j in range(sutun):
#         if i >= j:
#             asagi_ucbucaq_matris[i][j] = saygac_
#         saygac_ += 1
# print(yuxari_ucbucaq_matris)
#
# print(asagi_ucbucaq_matris)
#
# for row in asagi_ucbucaq_matris:
#     print(row)

# -----------------------------------------------------------------------------------

# setir = int(input("setir sayini daxil edin: "))
# sutun =  int(input("sutun sayini daxil edin: "))


# 1   0   1   0
# 0   1   0   1
# 1   0   1   0

# matris = []
#
# for i in range(setir):
#     sira = []
#     for j in range(sutun):
#         sira.append(0)
#     matris.append(sira)
#
# for i in range(setir):
#     for j in range(sutun):
#         if (i + j) % 2 == 0:
#             matris[i][j] = 1
#
# print(matris)
# for row in matris:
#     print(row)

# ------------------------------------------------------------------------------

# matris_1 = [[1, 2, 3], [4, 5, 6]]
# matris_2 = [[2, 3, 5], [3, 6, -8], [1, 2, 1]]
#
# for row in matris_1:
#     print(row)
# print()
# for x in matris_2:
#     print(x)
#
# yeni_matris = []
#

#
# a = int(input("a-ni daxil edin: "))
# b = int(input("b-ni daxil edin: "))
#
# mylist = []
#
# for i in range(a, b):
#     for j in range(2, i):
#         if i % j == 0 and int(str(i)[::-1]) % j == 0:
#             continue
#
#
# print(mylist)

# import random

# ad = input("Adi daxil edin:")
# soyad = input("Soyadi daxil edin: ")
# birthday = input("dogum tarixi: ")
# fin = input("fin: ")
# mystr = ""
#
# mystr += ad + soyad + birthday + fin
# parol_str = ""
# for i in mystr:
#     if i.isalnum():
#         parol_str += i
# sifre = random.sample(parol_str, 7)
# print("".join(sifre))

# ----------------------------------------------------------

# import random
#
# while True:
#     number = random.randint(10, 1000000000)
#     if len(str(number)) % 2 == 0:
#         print(number)
#         break

# ----------------------------------------------------------------


"""
3cu meselede alinan cut sayda reqemden ibaret ededdde ilk reqemden baslayaraq her bir reqem ozunden
sonraki reqemin sayini gosterirse bu saylari yazmaqla alinan yeni ededi cap edin

# 251430
# 554000
"""

# num_str = str(number)
# son_eded = ""
# for i in range(len(num_str)):
#     if int(i) % 2 == 0:
#         son_eded += str(int(num_str[i]) * str(num_str[i+1]))
# print(son_eded)

# -----------------------------------------------------------------------------

"""
matris1 = [
                [1,2],
                [7,3]
            ]
matris2 = [
                [2,3,6,4],
                [3,6,-8,5],
            ]
z[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0]
z[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1]
z[0][2] = x[0][0] * y[0][2] + x[0][1] * y[1][2]
z[0][3] = x[0][0] * y[0][3] + x[0][1] * y[1][3]

z[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0] 
z[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1]
z[1][2] = x[1][0] * y[0][2] + x[1][1] * y[1][2]
z[1][3] = x[1][0] * y[0][3] + x[1][1] * y[1][3]

z = [

    [z[0][0],z[0][1], z[0][2], z[0][3]],
    [z[1][0], z[1][1], z[1][2], z[1][3]]

    ]
"""


# matris1 = [
#                 [1,2],
#                 [7,3]
#             ]
# matris2 = [
#                 [2,3,6,4],
#                 [3,6,-8,5],
#             ]
#
# z = [[],[],[]]
#
# for i in range(len(matris1)):
#     for j in range(len(matris1[0])):
#         for a in range(len(matris2[0])):
#             pass


# ----------------------------------------------------------
# num = int(input("Ededi daxil edin: "))
#
# num_str = str(num)
# bos_str = ''
# for i in range(len(num_str)):
#     uzunluq = len(num_str)
#     sagda_qalan_reqemler_sayi = uzunluq - i - 1
#     bos_str += str(int(num_str[i]) * (10 ** sagda_qalan_reqemler_sayi))
#     print(bos_str)
#
# print(bos_str)

# -----------------------------------------------------------------

# 4000500708
# 4578

# eded = input("Ededi daxil edin: ")
# saygac = 0
# teze_eded = 0
# for i in range(len(eded)):
#     if eded[i] == 0:
#         saygac += 1
#
#     saygac = 0


# import matplotlib.pyplot as plt
# import numpy as np
#
# # 3x3 boyutunda matris oluşturma
# matrix = np.zeros((3, 3))
# # Matrisi çizme
# plt.imshow(matrix, cmap='binary', interpolation='none')
# plt.xticks(range(3))
# plt.yticks(range(3))
# plt.grid(True)
# plt.show()
#
# # Oyuncuların hamleleri
# matrix[0][0] = 1
# matrix[1][1] = 2
#
# # Matrisi güncelleme ve tekrar çizme
# plt.imshow(matrix, cmap='binary', interpolation='none')
# plt.xticks(range(3))
# plt.yticks(range(3))
# plt.grid(True)
# plt.show()

# matris = [
#     [-3, -2, 6],  # setir
#     [2, 1, 2],  # setir
#     [5, -2, -4]  # setir
#     #  sutun
# ]
#
# minimum_deyerler_setir_list = []
# for setir in matris:
#     minimum_deyerler_setir_list.append(min(setir))
#
# maksimum_deyerler_sutun_list = []
# for sutun in zip(*matris):
#     maksimum_deyerler_sutun_list.append(max(sutun))
#
#
# def simplex_function():
#     pass
#
# # Burda yoxlayaq gorek listlerden maks ve min deyerler birbirine beraberdirmi ?
#
# def netice(maks, minimum):
#     if maks == minimum:
#         return f"Hell noqtesi: {maks}"
#     simplex_function()
#
#
#
# print(netice(max(minimum_deyerler_setir_list), min(maksimum_deyerler_sutun_list)))


# # Mükafatlar
# T = 5   # İddia
# R = 3   # Mükafat
# P = 1   # Cəza
# S = 0   # Adi dəyər
#
# # Strategiyaların müəyyənləşdirilməsi
# C = 0   # Birlik
# D = 1   # Ayrılıq
#
# # Oyun matirisimizin müəyyənləşdirilməsi
# game_matrix = {
#     (C, C): (R, R),
#     (C, D): (S, T),
#     (D, C): (T, S),
#     (D, D): (P, P)
# }
#
# # Oyunçuların  hal-hazırki strategiyaları
# player1_strategy = C
# player2_strategy = D
#
# # Mükafatların əldə edilməsi
# player1_payoff, player2_payoff = game_matrix[(player1_strategy, player2_strategy)]
#
# # Nəticələrin çapı
# print(f"Player 1 strategy: {player1_strategy}")
# print(f"Player 2 strategy: {player2_strategy}")
# print(f"Player 1 payoff: {player1_payoff}")
# print(f"Player 2 payoff: {player2_payoff}")


# cumle = input("Cumleni daxil et: ")
#
# cumle_list = cumle.split()
#
# en_uzun_str = ''
#
# for soz in cumle_list:
#     if len(soz) > len(en_uzun_str):
#         en_uzun_str = soz
#
# matris = []
# for i in range(len(cumle_list)):
#     setir = []
#     for j in range(len(en_uzun_str)):
#         setir.append("*")
#     matris.append(setir)
#
# for i in range(len(cumle_list)):
#     for j in range(len(en_uzun_str)):
#
# print(matris)

# print(matris)
#
#
# print(matris)


# random_ededler = random.sample(range(1, 11), 7)
#
# for i in range(len(random_ededler)):
#     for j in range
# -------------------------------------------------------------------


# from scipy.optimize import linprog


# c = [-2, -3, -4]
#
# A = [[3, 2, 1], [2, 5, 3], [4, 2, 2]]  # 3x1 + 2x2 + x3 <= 10, 2x1 + 5x2 + 3x3 <= 15, 4x1 + 2x2 + 2x3 <= 8
# b = [10, 15, 8]
#
# x1_serhed = (0, None)  # x1 >= 0
# x2_serhed = (0, None)  # x2 >= 0
# x3_serhed = (0, None)  # x3 >= 0

# simpleks metodu tetbiqi
# result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_serhed, x2_serhed, x3_serhed], method='highs')

# print("Optimal deyer:", -result.fun)


# ---------------------------------------------------------------------------


# def harmonic_mean(lst):
#     cem = 0
#
#     def inverse_sum(lst):
#         nonlocal cem
#
#         for i in lst:
#             if i != 0:
#                 cem += (1 / i)
#
#         return len(lst)/cem
#
#     return inverse_sum(lst)
#
#
# mylist = [4, 6, 32, 2, 9, 0]
# print(harmonic_mean(mylist))


# -----------------------------------------------------------------

def four_metrics(lst):
    def mean(lst):
        return sum(lst) / len(lst)

    def median(lst):
        if len(lst) % 2 != 0:
            return sorted(lst)[len(lst) // 2]
        return (sorted(lst)[len(lst) // 2] + sorted(lst)[len(lst) // 2 - 1]) / 2

    def moda(lst):
        max_tekrar = 0
        for i in lst:
            if lst.count(i) > 1 and lst.count(i) > max_tekrar:
                max_tekrar = i
        return max_tekrar

    def diapazon(lst):
        return max(lst) - min(lst)

    return [median, mean, moda, diapazon]


mylist = [4, 6, 2, 23, 0, 1, 9, -5, 2]

# m1 = four_metrics(mylist)[0]
# m2 = four_metrics(mylist)[1]
# m3 = four_metrics(mylist)[2]
# m4 = four_metrics(mylist)[3]
#
# print(m1(mylist))
# print(m2(mylist))
# print(m3(mylist))
# print(m4(mylist))

# --------------------------------------------------------------

#
# def findelem(n):
#
#     if n == 1:
#         return 2
#     return findelem(n-1) + 3
#
# print(findelem(5))


# ------------------------------------------------------------

# def sum_with_rec(lst):
#     if len(lst) == 0:
#         return 0
#     return lst[0] + sum_with_rec(lst[1:])
#
#
# mylist = [2, 4, 56, 73, -56, 34]
# print(sum_with_rec(mylist))


# --------------------------------------------------------------
# 3, 7, 15, 31, ... ədədi ardıcıllığının istənilən nömrədəki elementini qaytaran rekursiv funksiya tərtib edin.
#     İnput: 3                 İnput: 6
#     Output: 15			   Output: 127


# a1 = 3
# a2 = a1 + 2 ** 1
# a3 = a2 + 2 ** 2
# a4 = a3 + 2 ** 3
# ...
# an = an-1 + 2**n-1


# def num_find_rec(n):
#     if n == 1:
#         return 3
#     return num_find_rec(n - 1) + 2 ** n
#
#
# print(num_find_rec(3))


# --------------------------------------------------------

# 6) 5-ci məsələdəki ədədi ardıcıllığın istənilən nömrəsinədək olan bütün elementlərini çap edən rekursiv funksiya tərtib edin.
#     İnput: 3                     İnput: 6
#     Output: 3 7 15		       Output: 3  7  15  31   63   127


# def nums_rec(n):
#     if n == 1:
#         return 3
#     return nums_rec(n - 1) + 2 ** n
#
#
# print(nums_rec(6))
#
# def print_sequence(n):
#     if n == 1:
#         return 3
#     else:
#         print_sequence(n-1)
#         element = 2**n - 1
#         print(element, end=" ")
#
# # Örnek kullanım
# print_sequence(7)
# -----------------------------------------------
# def mean(lst):
#     mean_value = sum(lst) / len(lst)
#     return mean_value
#
#
# def mean_diff_sqr(mean, lst):
#     new_list = []
#     for i in lst:
#         new_list.append((i-mean(lst))**2)
#
# def std(mean_diff_sqr, mean):
#     x = lambda lst:

# ----------------------------------------------

# 5)  3, 7, 15, 31, ... ədədi ardıcıllığının istənilən nömrədəki elementini qaytaran rekursiv funksiya tərtib edin.
#     İnput: 3                     İnput: 6
#     Output: 15			        Output: 127


# a1 = 3
# a2 = a1 + 2 ** 1
# a3 = a2 + 2 ** 2
# a4 = a3 + 2 ** 3
# ...
# an = an-1 + 2**n


# def find_num_rec(n):
#     if n == 1:
#         return 3
#     return find_num_rec(n-1) + 2**n
#
# print(find_num_rec(3), find_num_rec(6))


# ---------------------------------------------------


# paskal = [
#
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#
# ]
#
#
# def pascal_ucbucagi(n):
#     triangle = []
#     for i in range(n):
#         row = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 row.append(1)
#             else:
#                 element = triangle[i - 1][j - 1] + triangle[i - 1][j]
#                 row.append(element)
#         triangle.append(row)
#     return triangle
#
#
# print(pascal_ucbucagi(4))


# ------------------------------------------------------


# def mult_with_rec(num1, num2):
#     if num1 == 0 or num2 == 0:
#         return 0
#     return num1 + mult_with_rec(num1, num2 - 1)
#
#
# print(mult_with_rec(11, 6))


# def myfunc(num, exponent):
#     if exponent == 0:
#         return 1
#     return num * myfunc(num, exponent - 1)
#
#
# print(myfunc(3, 4))


#
# def cem_cut(n):
#     if n == 0:
#         return 0
#     else:
#         son_reqem = n % 10
#         if son_reqem % 2 == 0:
#             return son_reqem + cem_cut(n // 10)
#         else:
#             return cem_cut(n // 10)
#
#
# def tek_hasil(n):
#     if n == 0:
#         return 1
#     else:
#         son_reqem = n % 10
#         if son_reqem % 2 != 0:
#             return son_reqem * tek_hasil(n // 10)
#         else:
#             return tek_hasil(n // 10)
#
#
# print(cem_cut(23454))
# print(tek_hasil(23454))
# x = 10
# result = "Böyük" if x > 10 else "beraber" if x == 10 else "kicik"
# print(result)
#
# num = 153
# is_armstrong = lambda num: "Armstrongdur" if sum(
#     int(reqem) ** len(str(num)) for reqem in str(num)) == num else "Armstrong deyil"
# print(is_armstrong(num))
# #
# #
# arm_nums = lambda left, right, is_armstrong: [num for num in range(left, right) if is_armstrong(num) == "Armstrongdur"]
# print(arm_nums(100, 1000, is_armstrong))
#

# myfunc = lambda num: int("".join(reqem for reqem in str(num) if int(reqem) % 2 == 0))
# print(myfunc(5486945))

myfunc = lambda num: int("".join(reqem for reqem in str(num) if int(reqem) in [2, 3, 5, 7]))
print(myfunc(234636357))


# -------------------------------------------------------------------------

# def matris_rec(n1, n2):
#     if n1 == 1 and n2 == 1:
#         return [1]
#     return


# import numpy as np


# def kapitsa_model(hazirki_ehali, dogum_derecesi, olum_derecesi, miqrasiya_derecesi, years):
#     population = [hazirki_ehali]
#
#     for year in range(1, years + 1):
#         dogumlar = population[year - 1] * dogum_derecesi
#         olumler = population[year - 1] * olum_derecesi
#         mqirasiyalar = population[year - 1] * miqrasiya_derecesi
#
#         new_population = population[year - 1] + dogumlar - olumler + mqirasiyalar
#         population.append(new_population)
#
#     return population
#
#
# # Başlanğıc əhali sayı
# hazirki_ehali = 10000000
#
# # Doğum dərəcəsi
# dogum_derecesi = 0.02
#
# # Ölüm dərəcəsi
# olum_derecesi = 0.01
#
# # Göç dərəcəsi
# miqrasiya_derecesi = 0.005
#
# # Proqnozlaşdırılacaq illərin sayı
# years = 10
#
# # Kapitsa modelinin tətbiqi
# poplulyasiya_neticesi = kapitsa_model(hazirki_ehali, dogum_derecesi, olum_derecesi, miqrasiya_derecesi, years)
#
# # Proqnozlaşdırılmış əhali sayı çıxışı
# for year in range(len(poplulyasiya_neticesi)):
#     print(f"{year}: {int(poplulyasiya_neticesi[year])}")
#
#
#
#
#

# num = int(input("eded: "))
#
# print("boyuk" if num > 5 else "beraber" if num == 5 else "kicik")

# def sup_func(x, y):
#     return x ** y
#
#
# print(sup_func(y=4, x=3))


# ----------------------------------

#


def sade_eded(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


# #
# #
# # free_str = ""
# myfunc = lambda num: [reqem if sade_eded(int("".join(reqem) for reqem in str(num))) == True]
myfunc = lambda num: ["".join(reqem) for reqem in str(num) if sade_eded(int("".join(reqem)))]
print(myfunc(2351))

# # print(list(myfunc(4582)))
# yas = 25.3
#
# mesaj = "Mənim adım %s və mənim yaşım %d." % (ad, yas)
# print(mesaj)
#
# print(i for i in (1, 2, 3))
a = 3
print(f"salam {a}")
print("salam {}".format(a))
print("salam %d" %a)
