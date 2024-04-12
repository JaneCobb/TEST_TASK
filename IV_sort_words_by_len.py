# 4. Написать программу, которая сортирует список строк по длине,
# сначала по возрастанию, а затем по убыванию.
# задачка на порядок интересней и сложнее прошлых :)
from pprint import PrettyPrinter


def quicksort(words, order_by="ASC"):
    """Не очень понял задачу, если речь про самостоятельную реализацию
    какого либо алгоритма сортировки то вот:
    темп в лучшем случае O(n log n)
    """
    if len(words) < 2:
        return words
    else:
        pivot_el = words[0]
        less_pvt = [word for word in words if len(word) < len(pivot_el)]
        equal_pvt = [word for word in words if len(word) == len(pivot_el)]
        greater_pvt = [word for word in words if len(word) > len(pivot_el)]
        if order_by == "DESC":
            return quicksort(greater_pvt, order_by) + equal_pvt + [pivot_el]\
                 + quicksort(less_pvt, order_by)
        else:
            return quicksort(less_pvt, order_by) + equal_pvt + [pivot_el]\
                 + quicksort(greater_pvt, order_by)


def timsort_std(words, reverse=False):
    """ну а если речь про стандартную, то вот
    темп даже в худшем случае O(n log n), т.е он чаще будет быстрее"""
    return sorted(words, key=len, reverse=reverse)


if __name__ == "__main__":
    pretty_print = PrettyPrinter()
    frly = """So, take my love, take my land
    Take me where I cannot stand
    I don't care, I'm still free
    You can't take the sky from me
    Take me out into the black
    Tell 'em I ain't comin' back
    Burn the land and boil the sea
    You can't take the sky from me
    """.split()

    # quicksort alg
    sorted_asc = quicksort(frly)
    sorted_desc = quicksort(frly, order_by="DESC")
    print("\nQUICKSORT ASC: ", end="\n____________\n")
    pretty_print.pprint(sorted_asc)
    print("\nQUICKSORT DESC: ", end="\n____________\n")
    pretty_print.pprint(sorted_desc)

    # timsort
    timsort_asc = timsort_std(frly)
    timsort_desc = timsort_std(frly, reverse=True)
    print("\nTIMSORT ASC: ", end="\n____________\n")
    pretty_print.pprint(timsort_asc)
    print("\nTIMSORT DESC: ", end="\n____________\n")
    pretty_print.pprint(timsort_desc)
