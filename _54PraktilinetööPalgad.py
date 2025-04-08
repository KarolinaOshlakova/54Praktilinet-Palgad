from modulPalgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

#1
while True:
    print("andmed: ")
    print(inimesed) # выводим список имён
    print(palgad) # выводим список зарплат
    print("vajuta:\n1-andmete lisamiseks\n2-andmete kasutamiseks nime järgi") # предлагаем пользователю выбрать: 1 — добавить данные, 2 — удалить по имени
    v=int(input())
    if v==1: # если пользователь выбрал 1 — добавление данных
        k=int(input("mitu inimest?"))# спрашиваем, сколько людей нужно добавить
        for i in range(k):# запускаем цикл, повторяющийся k раз
            lisa_andmed(palgad,inimesed)
#2
while True:
    print("Andmed:")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1 - andmete lisamiseks\n2 - andmete kustutamiseks nime järgi\n3 - suurima palga leidmiseks")
    v = int(input())
    if v == 1:# если выбрано 1 — добавление данных
        k = int(input("Mitu inimest soovite lisada? "))
        for i in range(k):
            lisa_andmed(palgad, inimesed)
    elif v == 2: # если выбрано 2 — удаление данных по имени
        kustuta_andmed(palgad, inimesed)
    elif v == 3: # если выбрано 3 — поиск самой большой зарплаты
        suurim_palk(palgad,inimesed)
    else:# если введено что-то другое (не 1, 2, 3)
        print("Vale valik. Palun proovige uuesti.") # сообщение об ошибке выбора
#3
while True:
        if index >= len(p):
            break
        if p[index] == suurim: # если текущая зарплата равна самой большой зарплате
            print(f"Saab kätte: {i[index]}") # показываем имя человека, у которого такая зарплата
        index += 1 # переходим к следующей записи в списке
#4
while True:
        if index >= len(p):
            break
        if p[index] == väiksem:# Если текущая зарплата равна минимальной зарплате
            print(f"Saab kätte: {i[index]}") #Показываем имя человека с минимальной зарплатой
            p.pop(index) # Удаляем зарплату этого человека из списка p
            i.pop(index)# Удаляем имя этого человека из списка i
        else:
            index += 1# Если зарплата не минимальная, переходим к следующему человеку
#5
while True:
        sorted = False# Устанавливаем переменную чтобы отслеживать, были ли изменения
        for n in range(len(i)):  # Проходим по всем в списке людям(i)
            for m in range(n + 1, len(i)):
                if eval(str(p[n]) + v + str(p[m])):# Сравниваем зарплаты с помощью выражения в переменной v (например, ">" или "<")
                    p[n], p[m] = p[m], p[n]# Меняем местами зарплаты
                    i[n], i[m] = i[m], i[n]# Меняем местами имена, чтобы порядок совпадал с зарплатами
                    sorted = True# Если за весь цикл не было изменений значит, всё отсортировано
        if not sorted:
            break
        print("Järjestatud palgad ja nimed:")# Сообщаем, что данные отсортированы
for palk, nimi in zip(p, i): # Печатаем имена и зарплаты после сортировки
        print(f"{nimi}: {palk}")
#6
while True: 
        for n in range(len(p)): 
            nimed = [] 
            for m in range(len(p)): # Для каждого элемента в списке проверяем все остальные
                if p[m] == p[n] and m != n:  # Если зарплата человека m равна зарплате человека n и они разные
                    nimed.append(i[m])    # Добавляем имя из списка i в список nimed
            if nimed:  # Если в списке nimed есть хотя бы одно имя
                nimed.append(i[n]) # Добавляем имя человека n в список nimed
                print("Palk", p[n], ":", ', '.join(nimed), ". Kokku:", len(nimed), "inimest.")# Выводим зарплату, имена и количество людей с такой зарплатой
        jätkata = input("Kas soovite uuesti kontrollida? (jah/ei): ")  # Спрашиваем у пользователя, хочет ли он продолжить
        if jätkata.lower() != "jah": # Если пользователь ввёл не "jah", выходим из цикла
            break
#7
while True:
         nimi = input("Sisesta isiku nimi (või 'välja' lõpetamiseks): ") # Спрашиваем пользователя, введите ли имя
         if nimi.lower() == 'välja':  # Если введено välja, выходим из цикла
            print("Otsing lõpetatud.")# Выводим сообщение, что поиск завершён
            otsing = False 
         else:
            nimed = [] 
            for j in range(len(i)):# Проходим по всем именам в списке i
                if i[j] == nimi: # Если текущее имя совпадает с введённым пользователем
                    nimed.append(p[j])# Добавляем зарплату этого человека в список nimed
            if len(nimed) > 0: # Если в списке есть хотя бы одна зарплата
                print(nimi + " palk: " + ', '.join(map(str, nimed)) + ".")  # Выводим имена и их зарплаты
            else:
                print(nimi + " ei leitud.") # Если никого с таким именем не нашли, выводим, что не найдено
#8
while True:
    try:
        summa = float(input("Sisesta summa (nt 2000): "))  # Вводим сумму
        valik = input("Kas otsida rohkem (>'summa') või vähem (<'summa')? ")  # Спрашиваем, что искать: больше или меньше
        # Вызываем функцию, которая ищет людей по заданной зарплате
        otsi_inimesed(palgad, inimesed, summa, valik)#  ищеm людей по заданной зарплате
    except ValueError:  # Если введено что-то не то например, текст вместо числа
        print("Sisesta palun kehtiv arv.")  # Сообщаем об ошибке
    vastus = input("Kas soovite uuesti otsida? (jah/ei): ")# Спрашиваем пользователя, хочет ли он продолжить
    if vastus.lower() != "jah":  # Если ответ не "jah", то выходим
        break
#10
while True:
    print("\nValikud:")  # Печатаем меню
    print("1. Arvuta keskmine palk")  # для вычисления средней зарплаты
    print("2. Lõpeta")  # ля выхода из программы
    valik = input("Vali toiming (1 või 2): ")  # Спрашиваем, что выбрать
    if valik == "1":  # Если выбрали 1 (вычислить среднюю зарплату)
        # чтобы рассчитать и вывести среднюю зарплату
        keskmine(palgad, inimesed)
    elif valik == "2":  # Если выбрали 2 (выход)
        print("Programmi lõpetamine...")  # Сообщаем, что программа завершена
        break  # Прерываем цикл и завершаем программу
    else:  # Если выбрали что-то другое
        print("Vale valik, palun proovi uuesti.")  # Сообщаем, что выбор неверный и предлагаем попробовать снова
#9
while True:
    print("\nValikud:")
    print("1. Kuva T kõige vaesemad ja rikkamad inimesed")
    print("2. Lõpeta")
    valik = input("Vali toiming (1 või 2): ")

    if valik == "1":
        t = int(input("Sisesta, mitu inimest kuvada: "))# Запрашиваем количество людей для вывода
        top(palgad, inimesed, t) # Вызываем функцию top, которая и выводит нужных людей
    elif valik == "2":
        print("Programmi lõpetamine...")
        break
    else:
        print("Vale valik, proovi uuesti.")