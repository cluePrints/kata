def add(str_expression):
    res = 0
    if len(str_expression) > 0:
        for i in str_expression:
            if i != ",":
                res += int(i)
    return res

