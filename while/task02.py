our_dict = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Как успехи?": "Не легко",
    "Справишься?": "Конечно",
    "Удачи": "Спасибо"
}


def ask_user():
    while True:
        user_quest = input('Ваш вопрос: ')
        if user_quest in our_dict:
            print(our_dict[user_quest])
        else:
            print("Нужен другой вопрос :)")


ask_user()
