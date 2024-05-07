def computer_out(amount: int) -> str:
    last_two_digits: str = str(abs(amount))[-2:]
    exception_list = [str(x) for x in range(11, 15)]  # Числа от 11 до 14
    last_digit = last_two_digits[-1]

    if last_two_digits in exception_list:
        return f"{amount} компьютеров"
    elif int(last_digit) == 1:
        return f"{amount} компьютер"
    elif int(last_digit) in [2, 3, 4]:
        return f"{amount} компьютера"
    else:
        return f"{amount} компьютеров"


# test_amounts_list = [0, 1, 2, 3, 4, 5, 10, 11, 14, 21, 114, 124, -1, 82942]
# answers = '\n'.join(list(map(computer_out, test_amounts_list)))
# print(answers)
