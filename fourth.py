def multiplication_table(n):
    # Создание заголовка таблицы
    result_text = " \t"
    for i in range(1, n + 1):
        result_text += f"{i}\t"
    result_text += '\n'

    # Добавление строк таблицы
    for i in range(1, n + 1):
        result_text += f"{i}\t"
        for j in range(1, n + 1):
            result_text += f"{i * j}\t"
        result_text += '\n'
    return result_text


# print(multiplication_table(9))
