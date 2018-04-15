import random
import time

listaImion = ["kamila", "arek", "piotrek", "robert", "bartek"]

random.seed(time.time())
liczba = random.randrange(0, 11)
print(liczba)
print(random.choice(listaImion)) 