# 5. Kāda valsts nolēma pāriet uz jaunu naudas sistēmu. Vecajā sistēmā bija trīs naudas vienības: dālderis, grasis, santīms.
# Naudas vērtības norādītas zemāk.
# 1 dālderis = 37 graši
# 1 grasis = 162 santīmi
# Jaunajā naudas sistēmā paliek tikai santīmi un dālderi. Santīms saglabā savu vērtību, bet 1 dālderis būs vienāds ar 100 santīmiem.
# Izveidot programmu, kas pārveidotu vecās sistēmas naudu uz jaunu. Lietotājam prasa ievadīt vecās sistēmas dālderus, grašus un santīmus.
# Tiek aprēķināts jaunās sistēmas dālderu un grašu daudzums. Rezultāts tiek parādīts konsolē.
# 1 var
dalderis = int(input('Enter dālderi:'))
grasis = int(input('Enter graši:'))
santims = int(input('Enter santīmi:'))
santims += dalderis * 37 * 162
santims += grasis * 162
new_dalderis = santims // 100
new_santims = santims % 100
# vai
print(f'Jaunie dālderi: {new_dalderis}')
print(f'Jaunie santīmi: {new_santims}')
# vai
# print('Jaunie dālderi:', new_dalderis)
# print('Jaunie santīmi:', new_santims)

# 2 var
# dalderi = int(input('Dālderi: '))
# grasi = int(input('Graši: '))
# santimi = int(input('Santīmi: '))
# DALDERI_TO_GRASI = 37
# GRASI_TO_SANTIMI = 162
# NEW_DALDERI_TO_SANTIMI = 100
# santimi += dalderi * DALDERI_TO_GRASI * GRASI_TO_SANTIMI
# santimi += grasi * GRASI_TO_SANTIMI
#
# new_dalderi = santimi // NEW_DALDERI_TO_SANTIMI
# new_santimi = santimi % NEW_DALDERI_TO_SANTIMI
#
# print(f'Jaunie dālderi: {new_dalderi}')
# print(f'Jaunie santīmi: {new_santimi}')
