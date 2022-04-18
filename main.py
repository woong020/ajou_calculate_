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

global num_1
global num_2
global cal

idx = False

def isNumber(num):
  try:
    float(num)
    return True
  except ValueError:
    return False

def set_num1():     #num1 의 값을 받고 숫자가 아니면 종료
    global num_1
    num_1 = input("첫번째 숫자 : ")
    if isNumber(num_1) == True:
        num_1 = float(num_1)
    else:
        print("잘못 입력했습니다.")
        print("exit")
        sys.exit()  #프로그램 종료 함수
def set_num2():     #num2 의 값을 받고 숫자가 아니면 종료
    global num_2
    num_2 = input("두번째 숫자 : ")
    if isNumber(num_2) == True:
        num_2 = float(num_2)
    else:
        print("잘못 입력했습니다.")
        print("exit")
        sys.exit()
def prt_opt():      #옵션 번호 출력
    print("(1)더하기 (2)빼기 (3)곱하기 (4)나누기 (5)Clear (6)exit")
def set_opt():      #옵션 선택 호출
    global cal
    cal = input("연산 : ")
    #return cal

#add = calculate.Cal.__add__(num_1, num_2)

while True:
    if idx == False:        # 첫 실행시 bool idx == False << num1의 값을 입력받음
        set_num1()
        prt_opt()
        set_opt()

        if cal == '1':
            set_num2()
            num_1 = calculate.Cal.add(num_1, num_2)
            idx = True
        elif cal == '2':
            set_num2()
            num_1 = calculate.Cal.sub(num_1, num_2)
            idx = True
        elif cal == '3':
            set_num2()
            num_1 = calculate.Cal.mul(num_1, num_2)
            idx = True
        elif cal == '4':
            set_num2()
            num_1 = calculate.Cal.div(num_1, num_2)
            idx = True
        elif cal == '5':
            print("Clear")
            continue        #반복문 재실행
        elif cal == '6':
            break
        else :
            print("잘못 입력했습니다.")


    else:   #bool idx == True >> num_1 에 값이 입력된 상태
        print("첫번째 숫자 : %g" % (num_1))
        prt_opt()
        cal = input("연산 : ")
        if cal == '1':
            set_num2()
            num_1 = calculate.Cal.add(num_1, num_2)
        elif cal == '2':
            set_num2()
            num_1 = calculate.Cal.sub(num_1, num_2)
        elif cal == '3':
            set_num2()
            num_1 = calculate.Cal.mul(num_1, num_2)
        elif cal == '4':
            set_num2()
            num_1 = calculate.Cal.div(num_1, num_2)
        elif cal == '5':
            print("Clear")
            idx = False
            num_2 = 0
            continue
        elif cal == '6':
            print("exit")
            break
        else :
            print("잘못 입력했습니다.")
