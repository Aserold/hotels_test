def common_divisors(numbers: list) -> list:
    min_number = min(numbers)

    divisors = [dv for dv in range(1, min_number+1) if min_number % dv == 0]

    common_divisors = []
    for divisor in divisors:
        if all(number % divisor == 0 for number in numbers):
            common_divisors.append(divisor)
    common_divisors.pop(0)

    return common_divisors


# test_list = [42, 12, 18, 66]
# print(common_divisors(test_list))
