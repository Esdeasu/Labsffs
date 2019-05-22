import os
import os.path


def task1():
    fl = os.listdir(input("\nВведите директорию:\n\n - "))
    print("\nВ данной папке", len([n for n in fl if os.path.isfile(n)]), "файлов")


def task2(s1, s2):
    with open("products.txt", 'r') as prod:
        for line in prod:
            s1.append(line.rstrip())  # запись каждой строки как элемент списка без \n
        for i in range(0, len(s1)):
            s1[i] = s1[i].split(';')  # деление каждого элемента на список
    s2.append(s1[0])  # добавление заголовочного списка в конечный список
    s1.remove(s1[0])  # удаление заголовка из временного
    s1.sort(key=lambda s1: int(s1[2]))  # сортировка временного по int
    s2.extend(s1)  # добавление отсортированного в конечный
    print("\nОтсортированный список товаров:\n")
    for i in range(0, len(s2)):
        print(s2[i][0].ljust(3), s2[i][1].ljust(20), s2[i][2].ljust(6), s2[i][3].ljust(3))  # вывод
    return s1, s2


def task3(s1, s2):
    f = input("\nВведите номера товаров, которые Вы хотели бы уменьшить в кол-ве через пробел:\n\n - ")
    f = f.split()
    f = [int(i) for i in f if i.isdigit()]
    f = [i for i in f if i > 0 and i < len(s2)]
    n = int(input("\nНа сколько бы вы хотели уменьшить их кол-во?\n\n - "))
    s1.sort()  # обратная сортировка, номер товара совпадает с индексом в списке
    for i in range(0, len(f)):
        s1[f[i] - 1][3] = str(int(s1[f[i] - 1][3]) - n)
        if int(s1[f[i] - 1][3]) < 0:
            s1[f[i] - 1][3] = '0'
    s1.sort(key=lambda s1: int(s1[2]))  # сортируем обратно, делаем конечный список
    s2 = [s2[0]]
    s2.extend(s1)
    print("\nСписок с обновленным кол-вом товаров:\n")
    for i in range(0, len(s2)):
        print(s2[i][0].ljust(3), s2[i][1].ljust(20), s2[i][2].ljust(6), s2[i][3].ljust(3))
    return s1, s2


def task4(s1, s2):
    n = input('''\n\nКак бы вы хотели сохранить отсортированный список?
1) В тот же файл
2) В отдельный файл (будет создан в той же папке)
 - ''')
    if int(n) == 1:
        with open("products.txt", 'w') as prod:
            for i in range(0, len(s2)):
                prod.write(s2[i][0] + ';' + s2[i][1] + ';' + s2[i][2] + ';' + s2[i][3] + '\n')
        print("\nФайл успешно перезаписан!")
    elif int(n) == 2:
        with open('newfile.txt', 'w') as prod:
            for i in range(0, len(s2)):
                prod.write(s2[i][0] + ';' + s2[i][1] + ';' + s2[i][2] + ';' + s2[i][3] + '\n')
        print("\nФайл newfile.txt успешно создан")
    else:
        print("\nНекорректный ввод, принудительное завершение без сохранения")
    return s1, s2


k = int(input('''Выберите действие:
0 - Выход из программы
1 - Подсчет файлов в заданной директории
2 - Сортировка товаров из products.txt по цене
3 - Та же сортировка (2) + уменьшение кол-ва на заданное число
4 - (3) + сохранение изменений
 - '''))

while k != 0:
    s1 = []  # временный список, для начальной записи и последующей сортировки
    s2 = []
    if k == 1:
        task1()
    elif k in {2, 3, 4}:
        s1, s2 = task2(s1, s2)
        if k in {3, 4}:
            s1, s2 = task3(s1, s2)
            if k == 4:
                s1, s2 = task4(s1, s2)
    else:
        k = int(input("Введите корректный номер действия:\n\n - "))

    q = input("\nВы хотите продолжить? (Y, yes, 1 // N, no, 0)\n\n - ")
    if q in {'Y', 'yes', '1'}:
        k = int(input("\nВыберите действие из изначального списка:\n\n - "))
    elif q in {'N', 'no', '0'}:
        k = 0
    else:
        print("Некорректный ввод, принудительное завершение работы программы")
        k = 0
