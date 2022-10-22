#Лекция 1
def command_lesson_1():

    #Задание 1
    def lesson_1_task_1():
        print("Задание 1")
        box_length = int(input("Введите длину стороны квардрата: "))
        if box_length <= 0:
            print("Длина не может равняться 0 оибо быть меньше 0")
            return
        yardage_box = box_length ** 2
        print("Площадь квадрата состовляет: ", yardage_box)
        print()
        rectangle_length = int(input("Введите длину стороны прямоугольника: "))
        rectangle_width = int(input("Введите ширину стороны прямоугольника: "))
        if rectangle_length <= 0 or rectangle_width <= 0:
            print("Длина либо ширина, не может равняться 0 оибо быть меньше 0")
            return
        yardage_rectangle = rectangle_length * rectangle_width
        print("Площадь прямоугольника состовляет: ", yardage_rectangle)
        print( '#' * (yardage_box + yardage_rectangle) )
        print("Возврат в меню выбора задания")
        print(command_lesson_1())
        

    #Задание 2
    def lesson_1_task_2():
        print("Задание 2")
        wage = int(input("Введите заработную плату в месяц: "))
        mortgage = int(input("Введите, какой процент уходит на ипотеку: "))
        other_expenses = int(input("Введите, какой процент уходит на жизнь: "))
        print("Вывод:")
        print("На ипотеку было потрачено: ", (12*(wage * (mortgage / 100))) )
        print( "Было накоплено зa год: " , (wage * 12) - ((12*(wage * (mortgage / 100))) + (12*(wage * (other_expenses / 100)))) )
        print("Возврат в меню выбора задания")
        print(command_lesson_1())

    #Исполнения выбора задания
    print("В данном блоке 2 задания")
    id_task_lesson_1 = int(input("Введите задачу (1) или (2) либо (0) для выхода :"))
    if id_task_lesson_1 == 1:
        print(lesson_1_task_1())
    elif id_task_lesson_1 == 2:
        print(lesson_1_task_2())
    elif id_task_lesson_1 == 0:
        return "--END--"
    else:
        print("Данного задания нет или комманда введена неверно, повторите ввод")
        print(command_lesson_1())
    print("Выход в меню выбора лекции!")
    return "--End--"

#Лекция 2
def command_lesson_2():
    #Задание 1
    def lesson_2_task_1():

        interest_rate = 18.3
        region_true = 10
        children_amount = 3
        children_rate_true = 1
        salary_project_true = 0.5
        assurance_true = 1.5

        print("Задание 1:")
        print()
        print("Для рассчета процентной ставки пройдите небольшой опрос")
        region = input("Вы проживаете на терриротории Дальнего востока?: ").lower()
        if region == "да" or region == "lf":
            interest_rate -= region_true
            print("Процентная ставка для вас, составляет: ", interest_rate, "%")
            print("Возврат в меню выбора задания")
            print(command_lesson_2())

        elif region == 'нет' or region == 'ytn':

            children = input("У вас есть дети?: ").lower()
            if children == "да" or children == "lf":
                children_rate = int(input("Сколько у Вас детей?: "))
                if children_rate >= children_amount:
                    interest_rate -= children_rate_true
            salary_project = input("У вас есть зарплатный проект с нашим банком?: ").lower()
        
            if salary_project == 'да' or salary_project == 'lf':
                interest_rate -= salary_project_true
            assurance = input("желаете ли вы включить страховку?: ").lower()
            if assurance == 'да' or assurance == 'lf':
                interest_rate -= assurance_true
            
            print("Процентная ставка для вас, составляет: ", interest_rate, "%")
            print("Возврат в меню выбора задания")
            print(command_lesson_2())

    #Задание 1
    def lesson_2_task_2():
        print("Задание 2:")

        date = int(input("Введите дату от 1-31: "))
        month = input("Введите месяц (например: март): ").lower()

        if (date>=21 and date<=31 and month=="январь") or(date>=1 and date<=18 and month=="февраль"):
            print("Знак зодиака:Водолей")
        elif (date>=19 and date<=29 and month=="февраль") or(date>=1 and date<=20 and month=="март"):
            print("Знак зодиака:Рыбы")
        elif (date>=21 and date<=31 and month=="март") or(date>=1 and date<=19 and month=="апрель" ):
            print("Знак зодиака:Овен")
        elif (date>=20 and date<=30 and month=="апрель") or(date>=1 and date<=20 and month=="май"):
            print("Знак зодиака:Телец")
        elif (date>=21 and date<=31 and month=="май") or(date>=1 and date<=21 and month=="июнь"):
            print("Знак зодиака:Близнецы")
        elif (date>=22 and date<=30 and month=="июнь") or(date>=1 and date<=22 and month=="июль"):
            print("Знак зодиака:Рак")
        elif (date>=23 and date<=31 and month=="июль") or(date>=1 and date<=22 and month=="август"):
            print("Знак зодиака:Лев")
        elif (date>=23 and date<=31 and month=="август") or(date>=1 and date<=22 and month=="сентябрь"):
            print("Знак зодиака:Дева")
        elif (date>=23 and date<=30 and month=="сентябрь") or(date>=1 and date<=23 and month=="октябрь"):
            print("Знак зодиака:Весы")
        elif (date>=24 and date<=31 and month=="октябрь") or(date>=1 and date<=22 and month=="ноябрь"):
            print("Знак зодиака:Скорпион")
        elif (date>=23 and date<=30 and month=="ноябрь") or(date>=1 and date<=21 and month=="декабрь"):
            print("Знак зодиака:Стрелец")
        elif (date>=22 and date<=31 and month=="декабрь") or(date>=1 and date<=20 and month=="январь"):
            print("Знак зодиака:Козерог")
        print("Возврат в меню выбора задания")
        print(command_lesson_2())
        

    #Исполнения выбора задания
    print("В данном блоке 2 задания")
    id_task_lesson_2 = int(input("Введите задачу (1) или (2) либо (0) для выхода :"))
    if id_task_lesson_2 == 1:
        print(lesson_2_task_1())
    elif id_task_lesson_2 == 2:
        print(lesson_2_task_2())
    elif id_task_lesson_2 == 0:
        print("Выход в меню выбора лекции!")
        return "--End--"
    else:
        print("Данного задания нет или комманда введена неверно, повторите ввод")
        print(command_lesson_2())
 

#Список лекций
list_lessons = """"
Лекция 1 - Python. Знакомство с консолью 18.09.22
Лекция 2 - Условные конструкции. Операции сравнения 22.09.22
Лекция 3 - Циклы 29.09.22
"""
#Исполнение выбора лекции
while True:
    command_lesson = (input("Введите лекцию (1) или (2) или (3) и т.д.: "))
    if command_lesson == "1":
        print(command_lesson_1())
    elif command_lesson == "l":
        print(list_lessons)
    elif command_lesson == "2":
        print(command_lesson_2())
    else:
        print("Данной лекции нет. Список всех лекций можно посмтреть если ввести команду <<l>> - list")
    