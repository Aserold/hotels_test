
def prime_numbers(start: int, end: int) -> list:
    def is_prime(num: int) -> bool:
        """Проверка числа на простоту"""
        if num == 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    result = []
    for number in range(start, end + 1):
        if is_prime(number):
            result.append(number)
    return result


# print(prime_numbers(55, 331))
