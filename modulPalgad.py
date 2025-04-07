#1
p=[]
i=[]
def lisa_andmed(p:list,i=list):
    """
     :rtype: bool
    """
    while True:
       try:
           nimi=input("nimi: ")
           if nimi.isalpha():
            try:
                palk=float(input("palk: "))
            except:
                print:("palk on arv")
                print("andmed on lisatud")
       except:
        print("kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(i)
#2
    def kustuta_andmed(p:list,i:list):
        """
        :param p: Loend, kus on palgad.
        :param i: Loend, kus on inimeste nimed.
        :rtype: None
        """
        try:
            nimi=input("nimi: ")
            if nimi.isalpha():
                k=i.count(nimi)
                if k>0:
                    for j in range(k):
                        ind=i.index(nimi)
                        i.pop(ind)
                        p.pop(ind)
                    print("andmed on kasutatud")
                else:
                    print("andmed puuduvad")
        except:
            print("kirjuta ainult tähtede kasutades")
#3
def suurim_palk(p:list,i:list):
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    suurim=max(p)
    print(f"suurim palk on {suurim}")
    k=p.count(suurim)
    for j in range(k):
        ind=p.index(suurim)
        print(f"saab kätte{i[ind]}")
        ind=ind+1
#4
def väiksem_palk(p:list,i:list):
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    väiksem=min(p)
    print(f"väiksem palk on {väiksem}")
    k=p.count(väiksem)
    for j in range(k):
        ind=p.index(väiksem)
        print(f"saab kätte{i[ind]}")
        i.pop(ind)
        p.pop(ind)
#5
def sorteerimine(p: list, i: list)->any:
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    v=input("vali märk: > (kasvav) või < (kahanev)")
    for n in range(n,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
#6
def sama_palk(p: list, i: list):
    """
    :param p: Loend palgad.
    :param i: Loend nimed.
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"saab kätte {i[ind]}")
                ind+1
#7
def palk_nime_jargi(p: list, i: list):
     """
    :param p: Loend palgad.
    :param i: Loend nimed.
    """
     nimi = input("Sisesta isiku nimi (või 'välja' lõpetamiseks): ")
     if nimi.lower() == 'välja':
        print("Otsing lõpetatud.")
        return
     nimed = [] 
for j in range(len(i)):
        if i[j] == nimi:
            nimed.append(p[j]) 
            if len(nimed) > 0:
             print(nimi + " palk: " + ', '.join(map(str, nimed)) + ".")
else:
        print(nimi + " ei leitud.")
