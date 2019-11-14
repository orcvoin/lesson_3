# Заглавная буква для любого ввода


def int_func():
    text = input().title()
    print(text)


int_func()


print((lambda x: x.title())(input()))
