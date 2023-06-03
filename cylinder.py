import math

oturacaq_s = lambda r: math.pi * (r**2)

yan_s = lambda r, h: 2*math.pi*r*h

tam_s = lambda r, h: 2*math.pi*r*(r+h)

hecm = lambda r,h: ((math.pi)**2)*h


isci = {
    'Kenan': 1,
    'Tural': 2,
    'Yusif': 3,
}

sirket = ['Buta Group', 'Qmeter', 'MigrationPro']

with open('isciler', 'w', encoding='utf8') as fayl1:
    fayl1.write("isci = {\n")
    for key, value in isci.items():
        fayl1.write(f"    '{key}': '{value}',\n")
    fayl1.write("}\n\n")


with open('sirket', 'w', encoding='utf8') as fayl2:
    fayl1.write("sirket = {\n")
    for key, value in isci.items():
        fayl1.write(f"    '{key}': '{value}',\n")
    fayl1.write("}\n\n")