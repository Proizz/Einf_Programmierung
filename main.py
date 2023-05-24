
print("Übung a)")

cubics = [x**3 for x in range(10000, 0, -1) if x**3 % 5 == 0]
print(cubics)
print()

print("Übung b)")

import random

randoms = [random.randint(0, 10000) for x in range(0, 100)]
print(randoms)
print("Die größte Zahl ist ", (max(randoms)))
# alternativ
max_rand = -1
for rand in randoms:
    if max_rand < rand:
        max_rand = rand
print("Die größte Zahl ist ", max_rand)
print()

print("Übung c)")
print("Der Mittelwert ist ", sum(randoms)/len(randoms))
# alternativ
sum_rand = 0
for rand in randoms:
    sum_rand += rand
mittelwert = sum_rand/len(randoms)
print("Der Mittelwert ist ", mittelwert)
print()

print("Übung d)")
lottozahlen = [x for x in range(1, 50)]
picks = []
for i in range(0, 6):
    pick = random.choice(lottozahlen)
    lottozahlen.pop(lottozahlen.index(pick))
    picks.append(pick)
print(picks)
print()

print("Übung e)")


def reverse(wort):
    rev_wort = ""
    for i in range(-1, -len(wort)-1, -1):
        rev_wort += wort[i]
    return rev_wort


s = reverse("Justin Bieber")
print(s)
print()

print("Übung f)")


def ist_palindrom(inp_str):
    return inp_str == reverse(inp_str)


print(ist_palindrom("regalxager"))
print(ist_palindrom("regallager"))
print()

print("Übung f)")


def fibs(n):
    fibs = [1]
    if n == 1:
        return fibs
    fibs.append(1)
    for i in range(1, n-1):
        fibs.append(fibs[i]+fibs[i-1])
    return fibs


print(fibs(10))
