k = int(input("Введите количество элементов списка(N > 10) - "))
a = []
for i in range(0, k):
    a.append(input('Введите ' + str(i + 1) + ' элемент: '))
i = 0
while i < len(a):
    if int(a[i]) % 2 == 0:
        a.remove(a[i])
    else:
        i = i + 1
a.append(2)
a.append(3)
kk = len(a)
print('Итоговое количество элементов = ' + str(kk))
print(a)
