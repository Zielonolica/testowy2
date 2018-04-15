import random
import time

listaImion = ["kamila", "arek", "piotrek", "robert", "bartek", "grazynka"]

random.seed(time.time())
liczba = random.randrange(0, 11)
print(liczba)
print(random.choice(listaImion))
print(random.sample(listaImion, 2))