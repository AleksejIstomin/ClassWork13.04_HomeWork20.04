# 2. Zemniekam ir govis, cūkas un vistas. Govīm un cūkām ir pa 4 kājām, vistām – 2.
# Izveidot programmu, kas prasa lietotājam ievadīt cūku, govju un vistu skaitu. Tiek aprēķināts kopējais kāju daudzums. Rezultāts tiek izvadīts konsolē.

pigs = int(input('Enter amount of pig/pigs:'))
cows = int(input('Enter amount of cow/cows:'))
chickens = int(input('Enter amount of chicken/chickens:'))
legs = pigs*4 + cows*4 + chickens*2
print('Total amount of legs:', legs)
