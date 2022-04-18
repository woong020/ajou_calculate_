def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def cal_sum(cal_num_1, cal_num_2):
    print(cal_num_1, "+", cal_num_2, "=", sum(cal_num_1, cal_num_2))
    cal_num_1 = sum(cal_num_1, cal_num_2)
    return cal_num_1

def cal_sub(cal_num_1, cal_num_2):
    print(cal_num_1, "-", cal_num_2, "=", sub(cal_num_1, cal_num_2))
    cal_num_1 = sub(cal_num_1, cal_num_2)
    return cal_num_1

def cal_mul(cal_num_1, cal_num_2):
    print(cal_num_1, "*", cal_num_2, "=", mul(cal_num_1, cal_num_2))
    cal_num_1 = mul(cal_num_1, cal_num_2)
    return cal_num_1

def cal_div(cal_num_1, cal_num_2):
    print(cal_num_1, "/", cal_num_2, "=", div(cal_num_1, cal_num_2))
    cal_num_1 = div(cal_num_1, cal_num_2)
    return cal_num_1