# # 샘플 Python 스크립트입니다.
#
# # Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# # 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
#
#
# def print_hi(name):
#     # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
#     print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.
#
#
# # 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
import calculate
import sys

def cal_idx():
    global idx
    idx = False
def set_num1():
    global num_1
    num_1 = input("첫번째 숫자 : ")
    if num_1.isnumeric() == True:
        num_1 = int(num_1)
    else:
        print("잘못 입력했습니다.")
        print("exit")
        sys.exit()
def set_num2():
    global num_2
    num_2 = input("두번째 숫자 : ")
    if num_2.isnumeric() == True:
        num_2 = int(num_2)
    else:
        print("잘못 입력했습니다.")
        print("exit")
        sys.exit()
def prt_cal():
    print("(1)더하기 (2)빼기 (3)곱하기 (4)나누기 (5)Clear (6)exit")
def set_cal():
    global cal
    cal = input("연산 : ")


while True:
    if idx == False:        # 첫 실행
        set_num1()
        prt_cal()
        set_cal()

        if cal == '1':
            set_num2()
            print(num_1, "+", num_2, "=", calculate.sum(num_1, num_2))
            num_1 = calculate.sum(num_1, num_2)
            idx = True
            #continue
        elif cal == '2':
            set_num2()
            print(num_1, "-", num_2, "=", calculate.sub(num_1, num_2))
            num_1 = calculate.sub(num_1, num_2)
            idx = True
            #continue
        elif cal == '3':
            set_num2()
            print(num_1, "*", num_2, "=", calculate.mul(num_1, num_2))
            num_1 = calculate.mul(num_1, num_2)
            idx = True
            #continue
        elif cal == '4':
            set_num2()
            print(num_1, "/", num_2, "=", calculate.div(num_1, num_2))
            num_1 = calculate.div(num_1, num_2)
            idx = True
            #continue
        elif cal == '5':
            idx = False
            num_1 = 0
            num_2 = 0
            continue
        elif cal == '6':
            break

    else:
        print("첫번째 숫자 : ", num_1)
        prt_cal()
        cal = input("연산 : ")
        if cal == '1':
            set_num2()
            print(num_1, "+", num_2, "=", calculate.sum(num_1, num_2))
            num_1 = calculate.sum(num_1, num_2)
        elif cal == '2':
            set_num2()
            print(num_1, "-", num_2, "=", calculate.sub(num_1, num_2))
            num_1 = calculate.sub(num_1, num_2)
        elif cal == '3':
            set_num2()
            print(num_1, "*", num_2, "=", calculate.mul(num_1, num_2))
            num_1 = calculate.mul(num_1, num_2)
        elif cal == '4':
            set_num2()
            print(num_1, "/", num_2, "=", calculate.div(num_1, num_2))
            num_1 = calculate.div(num_1, num_2)
        elif cal == '5':
            print("Clear")
            idx = False
            #num_1 = int(input("첫번째 숫자 : "))
            num_2 = 0
            continue
        elif cal == '6':
            print("exit")
            break
