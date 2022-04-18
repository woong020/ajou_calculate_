import sys

def isNumber(num):
  try:
    float(num)
    return True
  except ValueError:
    return False

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
    def set_num_1(self):
        self.set_num_1 = input("첫번째 숫자 : ")
        if isNumber(self.set_num_1) == True:
            num_1 = float(self.set_num_1)
            return num_1
        else:
            print("잘못 입력했습니다.")
            print("exit")
            sys.exit()  # 프로그램 종료 함수

    def set_num_2(self):
        self.set_num_2 = input("두번째 숫자 : ")
        if isNumber(self.set_num_2) == True:
            num_2 = float(self.set_num_2)
            return num_2
        else:
            print("잘못 입력했습니다.")
            print("exit")
            sys.exit()

    def set_opt(self):
        self.set_opt = input("연산 : ")
        opt = self.set_opt
        return opt

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