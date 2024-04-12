# 2. Написать функцию, которая принимает на вход два целых числа
# (минимум и максимум) и возвращает список всех простых
# чисел в заданном диапазоне.
def is_simple_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def search_simple_nums(min_num, max_num: int):
    return [num for num in range(min_num, max_num + 1) if is_simple_num(num)]


if __name__ == "__main__":
    assert search_simple_nums(12, 15) == [13]  # True
    assert search_simple_nums(2, 5) == [2, 3, 5]  # True
    assert search_simple_nums(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]  # True
    # assert search_simple_nums(11, 12) == [12]  # False
