def str_to_int_list(str):
    lst = []
    collect = ""
    for i in str:
        if i in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            collect += i
        else:
            if len(collect) > 0:
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

