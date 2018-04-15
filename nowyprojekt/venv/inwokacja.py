print("hello", end='\n\n')
#zmienna = input('Podaj cos: ')
#print("To co podales to: {0}".format(zmienna))
tadzio = """Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
"""
print(tadzio)
dlugosc = len(tadzio)
print("Wielkość: {0}".format(dlugosc), end='\n\n')
tadzio = tadzio.replace('a', 'X')
print(tadzio)
ileDo = tadzio.count(' do ')
print("Ile 'do'? {0}".format(ileDo), end='\n\n')
print(tadzio.upper())