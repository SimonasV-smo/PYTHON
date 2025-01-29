
# Paprastas importavimas

import random

atsitiktinis_skaicius = random.randint(1, 10)
print(f"Atsitiktinis int skaičius nuo 1 iki 10: {atsitiktinis_skaicius}")

# Specifinių funkcijų importavimas

from random import randint, choice

atsitiktinis_skaicius = randint(1, 10)
atsitiktinis_elementas = choice(["sausis", "vasaris", "kovas"])

# Modulio trumpinimas naudojant alias

import random as rn

atsitiktinis_skaicius = rn.randint(20, 25)
atsitiktinis_elementas = rn.choice(["sausis", "vasaris", "kovas"])

# Specifinių funkcijų importavimas su alias

from random import randint as rnt

atsitiktinis_skaicius = rnt(1, 10)

# Visko importavimas iš modulio (nerekomenduojamas būdas)

from random import *

parinktis = sample(["sausis", "vasaris", "kovas"], k=3)
print(parinktis)

# Visas modulio importavimas

import aritmetikosmodulis

res = aritmetikosmodulis.dalink(10, 7)
print(res)

res = aritmetikosmodulis.daugink(10, 7)
print(res)

res = aritmetikosmodulis.atimk(10, 7)
print(res)

res = aritmetikosmodulis.sumuok(10, 7)
print(res)

# Specifinių funkcijų importavimas

from aritmetikosmodulis import dalink, daugink

res = dalink(10, 7)
print(res)

res = daugink(10, 7)
print(res)

# Modulio trumpinimas naudojant alias

import aritmetikosmodulis as ar

res = ar.dalink(10, 7)
print(res)

res = ar.daugink(10, 7)
print(res)

# Visas modulio importavimas iš folderio

import mylib.aritmetika

res = mylib.aritmetika.sumuok(10, 7)
print(res)

res = mylib.aritmetika.atimk(10, 7)
print(res)

# Specifinių funkcijų importavimas iš folderio

from mylib.aritmetika import dalink, daugink

res = dalink(10, 7)
print(res)

res = daugink(10, 7)
print(res)

# Modulio trumpinimas naudojant alias

import mylib.aritmetika as ar

res = ar.sumuok(10, 7)
print(res)

res = ar.atimk(10, 7)
print(res)

# Importavimas viso folderio

import mylib

res = mylib.aritmetika.sumuok(1, 5)
print(res)
