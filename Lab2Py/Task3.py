a = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса"
a = a.split(";_")
for i in range(0, len(a)):
    b = a[i].split(';')
    if i == 0:
        print(''.ljust(11) + b[0].ljust(19), b[1].ljust(18), b[2])
    else:
        if b[1] == '21 год':
            print(b[0].ljust(30), b[1].ljust(15), b[2])
