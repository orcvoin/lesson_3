# Задание 5
print('Введите целые числа через пробел, для выхода введите "x"')
total = 0


def numbers(text=input()):
    # global total
    summary = 0
    text = text.split()
    for i in text:
        try:
            i = float(i)
            summary = summary + i
        except ValueError:
            if type(i) == str:
                if i == 'x':
                    total = total + summary
                    print(total)
                    print('Завершено')
                    exit()
                print('Повторите попытку')
                return numbers(text=input())
            else:
                print('Завершено')
                exit()
    print('Введите целые числа через пробел')
    total = total + summary
    print(total)
    return numbers(text=input())


numbers()
