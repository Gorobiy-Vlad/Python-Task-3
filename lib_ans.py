def ANSWER_Y_N(str_answ):
    if str_answ == "Y":
        return True
    elif str_answ == "N":
        return False
    else:
        return None


def CHECK_NUMBER(inp_numbr, rand_numbr):
    if inp_numbr == rand_numbr:
        return True
    else:
        return False

def GAME(secrt_numbr, count):

    inp_answer = input("Введите предпологаемое, целое число: ")
    if inp_answer.isnumeric():
        if count > 1:
            if CHECK_NUMBER(int(inp_answer), secrt_numbr) == True:
                print("Поздравляю. Вы угадали!!!")

                while True:
                    answer = ANSWER_Y_N(input("Хотите повторить игру? (Y/N):"))
                    print("*" * 100)
                    if answer:
                        return None
                    elif answer is False:
                        print("Спасибо за игру)")
                        print("*" * 100)
                        return False
                    else:
                        print("Ведите корректный ответ!")
                        print("*" * 100)

            else:
                prompt = abs(int(inp_answer) - secrt_numbr)
                print("Вы не угадали. Попробуйте снова")
                if prompt > 10:
                    print("Холодно!")
                elif prompt > 5 and prompt < 10:
                    print("Тепло!")
                elif prompt < 4 and prompt > 1:
                    print("Гарячо!")
                return True
        else:
            print("*" * 100)
            return "Looser!"

    else:
        print("Введите целое число!")
        print("*" * 100)
        return True