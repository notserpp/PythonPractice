my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def less_than_ten():
    less_than_ten_list = []
    for x in my_list:
        if x < 10:
            less_than_ten_list.append(x)
    print less_than_ten_list


def less_than_give_number(number):
    less_than_number_list = []
    for x in my_list:
        if x < number:
            less_than_number_list.append(x)
    print less_than_number_list



less_than_give_number(35)
