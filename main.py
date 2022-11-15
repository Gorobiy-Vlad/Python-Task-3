import lib_ans
from random import randint as rand

# 1. В отдельном файле (пусть будет lib.py) написать функцию,
# которая требует от пользователя ответить да или нет ( Y\N ) и возвращает True\False
# в зависимости от того, что он ввел.
# В основном файле (пусть будет main_file.py) попросить пользователя ввести с клавиатуры строку
# и вывести ее на экран. Используя импортированную из lib.py функцию спросить у пользователя,
# хочет ли он повторить операцию (Y/N).Повторять пока пользователь отвечает Y
# и прекратить когда пользователь скажет N.


inp_str = input("Введите строку: ")
print(inp_str)
while True:
    inp_answer = input("Хотите ли повторить операцию? (Y/N): ")
    condition = lib_ans.ANSWER_Y_N(inp_answer)
    if condition:
        print(inp_str)
        print("*" * 100)
    elif condition is False:
        print("*" * 100)
        break
    else:
        print("Ведите корректный ответ!")
        print("*" * 100)


# 2. Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное число
# и предлагает пользователю его угадать. Пользователь вводит число.
# Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает.
# Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N - Прекратить.

print("Игра. Попробуйте угадать число")
condition = True

while condition:

    while True:
        try:
            counter = int(input("Введите колличество попыток (положительное, целое число): "))
            print("*" * 100)
            if counter <= 0:
                print("*" * 100)
                raise Exception("Количество попыток должно быть положительным!\n"
                                "Попробуйте снова")
            break
        except ValueError:
            print("*" * 100)
            print("Ошибка!\n"
                  "Количество попыток должно быть целым числом!\n"
                  "Попробуйте снова")
            print("*" * 100)
        except Exception as e:
            print(e)
            print("*" * 100)


    while True:
        try:
            start = int(input("Введите начало диапазона (целое число): "))
            end = int(input("Введите конец диапазона (целое число): "))
            secret_number = rand(start, end)
            print("*" * 100)
            print("Таинственный странник: Секретное число это ", secret_number)
            print("*" * 100)
            break
        except:
            print("*" * 100)
            print("Ошибка! Диапазон должен состоять из целых чисел. \n"
                  "И конец диапазона должен быть больше конца! \n"
                  "Попробуйте снова.")
            print("*" * 100)

    result = True
    while result:

        result = lib_ans.GAME(secret_number, counter)
        if result is False:
            condition = False
            break
        elif result is None:
            condition = True
            break
        else:
            counter = counter - 1
            print("Количество попыток: ", counter)
            if result == "Looser!":
                print("Looser!")
                condition = False
                break
            print("*" * 100)
