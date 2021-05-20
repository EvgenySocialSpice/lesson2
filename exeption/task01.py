def hello_user():
    while True:
        try:
            user_reply = input('Как дела? ')
            if user_reply == 'Хорошо':
                print('Пока')
                break
        except KeyboardInterrupt:
            print('Вы отменили операцию.')


hello_user()
