def search_for_negative(lst):
    for i in lst:
        if "-" in i:
            return True
    return False


def return_negativies(lst):
    result = ""
    for i in lst:
        if "-" in i:
            result += i
    return result


def str_to_int_list(str):
    lst = []
    collect = ""
    for i in str:
        if i in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"}:
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
        if search_for_negative(list_of_num):
            return "negatives not allowed: " + return_negativies(list_of_num)
        return sum_list(list_of_num)
    else:
        return 0


print(add("-34, 5, 6, 5"))
print(add("-34, -5, 6, 5"))
print(add("bh0,65/-7"))
