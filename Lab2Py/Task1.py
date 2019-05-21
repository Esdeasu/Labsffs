a = input("Введите строку - ")
a = a + " "
i = 0
o = ''
while i < len(a):
    k = 0
    if a[i] == 'Л' and a[i+1] == 'и':
        for b in a[i:]:
            if b != ' ' and b != ',' and b != '.':
                k = k + 1
            else:
                break
        o = o + a[i:i+k] + ' '
    i = i + 1
print(o)
