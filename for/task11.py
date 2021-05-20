age = int(input('Сколько вам лет: '))


def activity():
    if 0 < age < 6:
        return 'Тебе нужно в детский сад'
    elif 6 < age < 18:
        return 'Иди в школу учиться'
    elif 18 < age < 25:
        return 'Иди учиться в ВУЗ'
    else:
        return 'Иди работать'


print(activity())
