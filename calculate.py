class Default_Cal:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

class Cal:
    def add(cal_num_1, cal_num_2):
        print("%g + %g = %g" % (cal_num_1, cal_num_2, Default_Cal.add(cal_num_1, cal_num_2)))
        cal_num_1 = Default_Cal.add(cal_num_1, cal_num_2)
        return cal_num_1

    def sub(cal_num_1, cal_num_2):
        print("%g - %g = %g" % (cal_num_1, cal_num_2, Default_Cal.sub(cal_num_1, cal_num_2)))
        cal_num_1 = Default_Cal.sub(cal_num_1, cal_num_2)
        return cal_num_1

    def mul(cal_num_1, cal_num_2):
        print("%g * %g = %g" % (cal_num_1, cal_num_2, Default_Cal.mul(cal_num_1, cal_num_2)))
        cal_num_1 = Default_Cal.mul(cal_num_1, cal_num_2)
        return cal_num_1

    def div(cal_num_1, cal_num_2):
        print("%g / %g = %g" % (cal_num_1, cal_num_2, Default_Cal.div(cal_num_1, cal_num_2)))
        cal_num_1 = Default_Cal.div(cal_num_1, cal_num_2)
        return cal_num_1




# def cal_add(cal_num_1, cal_num_2):
#     print(cal_num_1, "+", cal_num_2, "=", add(cal_num_1, cal_num_2))
#     cal_num_1 = add(cal_num_1, cal_num_2)
#     return cal_num_1
#
# def cal_sub(cal_num_1, cal_num_2):
#     print(cal_num_1, "-", cal_num_2, "=", sub(cal_num_1, cal_num_2))
#     cal_num_1 = sub(cal_num_1, cal_num_2)
#     return cal_num_1
#
# def cal_mul(cal_num_1, cal_num_2):
#     print(cal_num_1, "*", cal_num_2, "=", mul(cal_num_1, cal_num_2))
#     cal_num_1 = mul(cal_num_1, cal_num_2)
#     return cal_num_1
#
# def cal_div(cal_num_1, cal_num_2):
#     print(cal_num_1, "/", cal_num_2, "=", div(cal_num_1, cal_num_2))
#     cal_num_1 = div(cal_num_1, cal_num_2)
#     return cal_num_1