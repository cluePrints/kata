def str_to_int_list(str):
    lst = []
    collect = ""
    for i in str:
        if i != ",":
            collect += i
        if i == ",":
            lst.append(collect)
            collect = ""
    lst.append(collect)
    return lst


def sum_list(lst):
    res = 0
    for i in lst:
        res += int(i)
    return res


def add(str_expression):
    if len(str_expression) >= 1:
        list_of_num = str_to_int_list(str_expression)
        return sum_list(list_of_num)
    else:
        return 0

