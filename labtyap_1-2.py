import random
p = random.randint(1,100)
print("ЗАГАДАНО ЧИСЛО ОТ 1 ДО 100. ПОПРОБУЙ ОТГАДАТЬ ИЛИ СДАЙСЯ ВВЕДЯ 101")
i=0
while i<1:
    a = int(input("ВВОД: "))
    if a == 101:
        print("БЕЛЫЙ ФЛАГ ПОДНЯТ! ВЫ ПРОИГРАЛИ ЧИСЛУ ",p); i=1
    elif a == p:
        print("GLORIOUS VICTORY"); i=1
    else:
        print("В МОЛОКО, ДАВАЙ ЕЩЕ РАЗОК")
    
    
