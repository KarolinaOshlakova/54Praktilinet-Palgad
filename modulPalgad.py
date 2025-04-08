#1
p=[]
i=[]
def lisa_andmed(p:list,i=list):
    """
     :rtype: bool
    """
    while True:# бесконечный цикл
       try:
           nimi=input("nimi: ") # просим ввести имя
           if nimi.isalpha(): # проверяем, что имя состоит только из букв
            try:
                palk=float(input("palk: ")) # просим ввести зарплату
            except:
                print("palk on arv")
                print("andmed on lisatud")# сообщение о том, что данные добавлены
       except:
        print("kirjuta ainult tähtede kasutades") # если ввод неправильный предупреждение
    p.append(palk) # добавляем зарплату в список
    i.append(i)
#2
    def kustuta_andmed(p:list,i:list):
        """
        :param p: Loend, kus on palgad.
        :param i: Loend, kus on inimeste nimed.
        :rtype: None
        """
        try:
            nimi=input("nimi: ") # спрашиваем имя у пользователя
            if nimi.isalpha(): # проверяем, что введено только из букв (без цифр и символов)
                k=i.count(nimi) # считаем, сколько раз это имя встречается в списке
                if k>0: # если имя есть хотя бы один раз
                    for j in range(k): # повторяем столько раз, сколько раз имя встречается
                        ind=i.index(nimi) # находим первого человека
                        i.pop(ind)# удаляем имя по этому индексу
                        p.pop(ind)# удаляем зарплату
                    print("andmed on kasutatud") # выводим, что данные удалены
                else:
                    print("andmed puuduvad") # если имя не найдено выводим, что данных нет
        except:
            print("kirjuta ainult tähtede kasutades")
#3
def suurim_palk(p:list,i:list):
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    suurim=max(p) # находим самую большую зарплату в списке
    print(f"suurim palk on {suurim}")  # выводим её на экран
    k=p.count(suurim)# считаем, сколько раз встречается эта зарплата
    for j in range(k):# повторяем цикл столько раз, сколько таких зарплат
        ind=p.index(suurim)# находим первого человека
        print(f"saab kätte{i[ind]}")# выводим имя человека по этому индексу
        ind=ind+1 # Переходим к следующему человеку в списке
#4
def väiksem_palk(p:list,i:list):
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    väiksem=min(p)  # Находим минимальную зарплату в списке p
    print(f"väiksem palk on {väiksem}")   # Выводим минимальную зарплату на экран

    k=p.count(väiksem)# Считаем, сколько раз эта минимальная зарплата встречается в списке
    for j in range(k): # Цикл, который выполняется столько раз, сколько раз минимальная зарплата встречается в списке
        ind=p.index(väiksem) # Находим первого человека, который получает минимальную зарплату
        print(f"saab kätte{i[ind]}")  # Выводим имя человека, который получает минимальную зарплату
        i.pop(ind) # Удаляем это имя из списка i 
        p.pop(ind) # Удаляем эту зарплату из списка p
#5
def sorteerimine(p: list, i: list)->any:
    """
    :param p: Loend, kus on palgad.
    :param i: Loend, kus on inimeste nimed.
    :rtype: None
    """
    v=input("vali märk: > (kasvav) või < (kahanev)")# просим пользователя выбрать знак: ">" для сортировки по возрастанию или "<" для сортировки по убыванию
    for n in range(n,len(i)): #начинаем цикл с первого элемента
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])): # Если зарплата в позиции n больше (или меньше, в зависимости от знака v) зарплаты в позиции m
                p[n],p[m]=p[m],p[n]# Меняем местами зарплаты в списке p
                i[n],i[m]=i[m],i[n]# Меняем местами имена в списке i, чтобы они соответствовали зарплатам которые сортировали
#6
def sama_palk(p: list, i: list):
    """
    :param p: Loend palgad.
    :param i: Loend nimed.
    """
    hulk=set(p) # создаём множество из списка зарплат, чтобы получить только зарплаты которые не повторяются

    print(hulk)# Выводим на экран все зарплаты
    for palk in hulk: #создаем цикл 
        k=p.count(palk)  # Считаем, сколько раз эта зарплата встречается в списке
        if k>1: #вводим условие, сколько раз эта зарплата встречается в списке
            print(f"palk {palk}") # Выводим эту зарплату на экран
            ind=p.index(palk)# Находим индекс первого человека, который получает эту зарплату
            for j in range(k): # вводим  цикл для каждого человека, который получает эту зарплату
                ind=p.index(palk,ind)
                print(f"saab kätte {i[ind]}")# Выводим имя этого человека, который получает эту зарплату
                ind+1 # Переходим к следующему человеку в списке
#7
nimi=[]
nimed=[]
def palk_nime_jargi(p: list, i: list):
     """
    :param p: Loend palgad.
    :param i: Loend nimed.
    """
     nimi = input("Sisesta isiku nimi (või 'välja' lõpetamiseks): ") # Просим пользователя ввести имя человека. Можно ввести välja для завершения поиска
     if nimi.lower() == 'välja': # Если пользователь вводит välja, то заканчиваем поиск
        print("Otsing lõpetatud.")
        return # Прерываем выполнение программы
     nimed = [] 
for j in range(len(i)):
        if i[j] == nimi: # Если текущее имя в списке совпадает с тем, что ввел пользователь
            nimed.append(p[j]) #  то добавляем зарплату из списка p, которая соответствует найденному имени
            if len(nimed) > 0:# Если в списке найденных зарплат есть хотя бы одна зарплата больше 0
             print(nimi + " palk: " + ', '.join(map(str, nimed)) + ".") # то выводим имя и его зарплаты (если их несколько, они будут разделены запятой)
else: # Если имя не найдено в списке, срабатывает эта часть и далее пишем не найдено
        print(nimi + " ei leitud.")
#8
def otsi_inimesed(p:list,i: list):
    """
    :param p: list, kus on inimeste palgad
    :param i: list, kus on inimeste nimed
    :param summa: float, summa, mille järgi otsitakse
    """
summa=[]
valik=[]
if valik == ">": # Если мы ищем людей, чья зарплата больше суммы
        print(f"Inimesed, kelle palk on suurem kui {summa}:")
        for j in range(len(p)):
            if p[j] > summa:  # Если зарплата больше
                print(f"{i[j]}: {p[j]}")  # Показываем имя и зарплату
elif valik == "<": # Если мы ищем людей, чья зарплата меньше суммы
        print(f"Inimesed, kelle palk on väiksem kui {summa}:")
        for j in range(len(p)):
            if p[j] < summa:  # Если зарплата меньше
                print(f"{i[j]}: {p[j]}")  # Показываем имя и зарплату
else:
        print("Vale valik. Palun sisesta > või <.")  #введён неправильный символ
#10
def keskmine(p:list,i: list):
    """
    Arvutab keskmise palga ja kuvab selle saaja nime või nimesid.
    :param p: list, kus on inimeste palgad 
    :param i: list, kus on inimeste nimed 
    """
    keskmine_palk = sum(p) / len(p)
    print(f"Keskmine palk on: {keskmine_palk}")  # Выводим среднюю зарплату
    leitud = False  #показывает, нашли ли мы людей с такой зарплатой
    for j in range(len(p)):  # Проходим по каждому человеку
        if p[j] == keskmine_palk:  # Если зарплата человека равна средней
            if not leitud:  # Если это первый такой человек
                print("Keskmist palka saab kätte: ", end="")
                leitud = True  # Помечаем, что нашли хотя бы одного человека
            print(f"{i[j]}", end=" ")  # Выводим имя этого человека
    if not leitud:  # Если никого не нашли, выводим сообщение
        print("Keegi ei saa täpselt keskmist palka.")
#9
def top(p:list,i: list):
    """
     Kuvab T kõige vaesemad ja rikkamad inimesed.
    :param p: list, palkade loend
    :param i: list, inimeste nimed
    :param t: int, kui palju inimesi kuvada
    """
    inimesed = list(zip(p, i))# Объединяем зарплаты и имена в пары
    inimesed.sort() # Сортируем людей по зарплатам
    print(f"T kõige vaesemad inimesed:") # Выводим T самых бедных людей
    for j in range(min(t, len(inimesed))):
        print(f"{inimesed[j][1]}: {inimesed[j][0]}")
    inimesed.sort(reverse=True) # Сортируем людей по зарплатам для самых богатых
    print(f"\nT kõige rikkamad inimesed:")# Выводим T самых богатых людей
    for j in range(min(t, len(inimesed))):
        print(f"{inimesed[j][1]}: {inimesed[j][0]}")