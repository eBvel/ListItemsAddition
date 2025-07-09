def create_list_of_numbers(stop):
    return [i for i in range(1, stop + 1)]


def adding_lists_items(list1, list2):
    short_list = list1 if len(list1) < len(list2) else list2
    short_list_length = len(short_list)
    result = [list1[i] + list2[i] for i in range(short_list_length)]
    result.extend(list1[short_list_length:] if short_list is list2
                  else list2[short_list_length:])

    return result


def adding_lists_items_v2(list1, list2):
    short_list = list1 if len(list1) < len(list2) else list2
    length_difference = abs(len(list1) - len(list2))
    short_list.extend([0 for _ in range(length_difference)])

    return [list1[i] + list2[i] for i in range(len(list1))]


def main():
    first_list_of_numbers = create_list_of_numbers(7)
    second_list_of_numbers = create_list_of_numbers(10)

    result = adding_lists_items(first_list_of_numbers, second_list_of_numbers)
    result_v2 = adding_lists_items_v2(first_list_of_numbers,
                                      second_list_of_numbers)
    print(f"\nРезультат сложения списков: {result}\nРезультат сложения списков v2: {result_v2}")


main()
