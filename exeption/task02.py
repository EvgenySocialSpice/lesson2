def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    try:
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except IndentationError:
        print('Максимальная скидка 99')
    except TypeError:
        print('Введены не все данные')
    except ValueError:
        print('Неверно введены данные')


print(discounted(1200, 111, 19))

