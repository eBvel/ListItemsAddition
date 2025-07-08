def create_list_of_numbers(stop):
    return [i for i in range(0, stop)]


def adding_lists_items(list1, list2):
    return [list1[i] + list2[i] for i in list1]


def main():
    first_list_of_numbers = create_list_of_numbers(20)
    second_list_of_numbers = create_list_of_numbers(20)

    result = adding_lists_items(first_list_of_numbers, second_list_of_numbers)
    print(f"\nРезультат сложения списков: {result}")


main()
