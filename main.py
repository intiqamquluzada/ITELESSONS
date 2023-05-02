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
print(44444)
print(55555)
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
#---------------------------------------------------------------------------------------

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

#------------------------------------------------------------------