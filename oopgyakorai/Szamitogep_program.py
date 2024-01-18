from Szamitogep import Szamitogep

peldany1 = Szamitogep("win", 32)
peldany1 = Szamitogep("mac", 16)
peldany1 = Szamitogep("win", 16)
szamitogepek = []
szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram}) ")

print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(round(gyujto/ len (szamitogepek),3))

print("Legtöbb ramot tartalmazó oprendszer: ")
index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[1].ram > szamitogepek[index].ram:
        index = i
print(szamitogepek[index].oprsz)