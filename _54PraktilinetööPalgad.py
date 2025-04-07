from modulPalgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

#1
while True:
    print("andmed: ")
    print(inimesed)
    print(palgad)
    print("vajuta:\n1-andmete lisamiseks\n2-andmete kasutamiseks nime järgi")
    v=int(input())
    if v==1:
        k=int(input("mitu inimest?"))
        for i in range(k):
            lisa_andmed(palgad,inimesed)
#2
while True:
    print("Andmed:")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1 - andmete lisamiseks\n2 - andmete kustutamiseks nime järgi\n3 - suurima palga leidmiseks")
    v = int(input())
    if v == 1:
        k = int(input("Mitu inimest soovite lisada? "))
        for i in range(k):
            lisa_andmed(palgad, inimesed)
    elif v == 2:
        kustuta_andmed(palgad, inimesed)
    elif v == 3:
        suurim_palk(palgad,inimesed)
    else:
        print("Vale valik. Palun proovige uuesti.")
#3
while True:
        if index >= len(p):
            break
        if p[index] == suurim:
            print(f"Saab kätte: {i[index]}")
        index += 1
#4
while True:
        if index >= len(p):
            break
        if p[index] == väiksem:
            print(f"Saab kätte: {i[index]}")
            p.pop(index)
            i.pop(index)
        else:
            index += 1
#5
while True:
        sorted = False
        for n in range(len(i)):
            for m in range(n + 1, len(i)):
                if eval(str(p[n]) + v + str(p[m])):
                    p[n], p[m] = p[m], p[n]
                    i[n], i[m] = i[m], i[n]
                    sorted = True
        if not sorted:
            break

        print("Järjestatud palgad ja nimed:")
for palk, nimi in zip(p, i):
        print(f"{nimi}: {palk}")
#6
while True: 
        for n in range(len(p)): 
            nimed = [] 
            for m in range(len(p)): 
                if p[m] == p[n] and m != n:  
                    nimed.append(i[m])  
            if nimed: 
                nimed.append(i[n]) 
                print("Palk", p[n], ":", ', '.join(nimed), ". Kokku:", len(nimed), "inimest.")
        jätkata = input("Kas soovite uuesti kontrollida? (jah/ei): ")
        if jätkata.lower() != "jah": 
            break
#7
while True:
         nimi = input("Sisesta isiku nimi (või 'välja' lõpetamiseks): ")
         if nimi.lower() == 'välja':
            print("Otsing lõpetatud.")
            otsing = False 
         else:
            nimed = [] 
            for j in range(len(i)):
                if i[j] == nimi:
                    nimed.append(p[j])
            if len(nimed) > 0:
                print(nimi + " palk: " + ', '.join(map(str, nimed)) + ".")
            else:
                print(nimi + " ei leitud.")