def task1():
    num=int(input("Введите число:"))
    if num%3==0:
        print("Число делится на 3!")
    else:
        print("Число не делится на 3(")


def task2():
    while True:
        try:
            num = int(input("Введите число:"))
            nnum = (100/num)
        except ZeroDivisionError:
            print("Деление на 0 невозможно!")
        except ValueError:
            print("Это не число!")
        else:
            print(nnum)


def task3():
    day = str(input("Введите день"))
    month = str(input("Введите месяц"))
    year = str(input("введите год"))
    yearnew = int(str(year)[2:])
    daynow = int(str(day))
    monthnow = int(str(month))
    if yearnew==daynow*monthnow:
        print("Это магическая дата!")
    else:
        print("Это не магическая дата :(")


def task4():
    ticket = str(input("Введите номер билета"))
    haif1 = int(str(ticket)[:len(ticket)//2])
    haif2 = int(str(ticket)[len(ticket) // 2:])
    haif1new = list(map(int, str(haif1)))
    haif2new = list(map(int, str(haif2)))
    if sum(haif1new)==sum(haif2new):
        print("Ваш билет счастливый!")
    else:
        print("Ваш билет не счастливый")


task1()
task2()
task3()
task4()