'''
1. 함수(function) : 특정 작업을 수행하는 코드 블록을 정의하는 방법
ex) 사진을 찍는다 라는 행위
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고.
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누른다.
그런데 컴퓨터는 시키는 대로만 하기 때문에 사진을 찍기 위해서
1~5 까지의 명령어를 입력해줘야만 합니다.
하지만 그 함수 내에의 명령어를 미리 입력해두고 나서 ,
명령어를 실행 시키기만 하면 순서대로 수행하도록 하는 것이 함수의 개념이라고 할 수 있겠습니다.

함수 정의 형식 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()
함수 호출 형식 :
turn_right()
2. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(method)
    3) 사용자 정의 함수
3. 함수 용어 정리 (멘토 파이썬 교재)
    1) 함수 정의 : 사용자 함수를 새로 만드는 것 (def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값(return) : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것
4. (사용자) 함수의 형식 :
def 함수_의미(매개변수):
    실행문

변수 = 함수_이름(argument)
'''
from idlelib.configdialog import changes

# # 함수 정의
# def write_name(name):                 # 정의할 때 소괄호 내에 있는 것을 parameter 라고 합니다
#     print(f"당신의 이름은 {name}입니다.")
# # 함수 호출
# write_name("김재우")                   # 호출할 때 소괄호 내에 있는 것을 argument 라고 합니다.
#
# def write_name_age(name,age):         #parameter 가 복수인 사례
#     print(f"당신의 이름은 {name}, 이고 나이는 {age}살 입니다.")
#
# write_name_age("김재우",38)    # 매개변수가 두 개 이기 때문에 argument 도 두 개 인 상황
# write_name_age(age= 10,name="안근수")    # keyword argument 라고 함
'''
ex)  input("이름을 입력하세요 >>>")을 이용해서 이것을 name 이라는 변수에 담았다고 가정하면.
name = input("이름을 입력하세요 >>>") 이라고 작성해왔습니다.
이때까지는 함수의 결과값을 변수에 담아오고 있었음
파이썬 내장 함수에는 이미 함수가 정의 돼있고, 개발자들은 함수를 호출만 잘 하면 끝.
사용자 함수는 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각

내장함수 ex) print() / type() / int() / flat() / input()
2. 메서드(method) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함한 함수.
사실 함수와 메서드는 동일한 개념, 호출 방식의 차이
함수는 독림적 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능 
# '''
# eng_name = input("당신의 이름을 소문자로 입력하세요 >>>").upper()  # input() = 함수/ .upper() = 메서드
# print(eng_name) # 함수
# eng_name2 = input("당신의 이름을 소문자로 입력하세요 >>>").title()
# print(eng_name2)
'''
함수(메서드)의 유형
'''
# #  매개변수 x / 리턴 x
# def call1():
#     print("[ x / x]")
# # 매개변수 o / 리턴 x
# def call2(str_type):
#     print("[ o / x]")
#     print(f"{str_type}이라고 입력하셨나보네요")
# # 매개변수 x / 리턴 o
# def call3():
#     print("[ x / o]")
#     return 1
# # 매개변수 o / 리턴 o
# def call4(str_type):
#     print("[ o / o]")
#     return f"제 이름은 {str_type}입니다."
# call1()
# call2("오늘 날씨가 너무 추워요")
# call3() # 이 경우 return이 출력되지 않음
# print(call3()) #이렇게 해야 return 출력
# print(call3() + 1)
#
# new_element = (call3() + 3 ) * 10
# print(new_element)
#
# call4("김재우")
# print(call4("김재우"))
#
'''
call3() / call4() 유형에서 함수내에 print()를 집어넣어두면 main 단계에서 (들여쓰기가 되어있지 않은 단계)
print() 함수를 입력할 필요가 없어 훨씬 편할 것 같은데
왜 굳이 return 형태로 입력해서 main 에서 print() 함수를 적용해야 하는가

함수형 프로그래밍 (Functional Programming) : 특정한 함수1의 결과값이 
    또 다른 함수2의 argument 로 사용되는 것을 의미
    함수2의 결과 값이 함수3의 argument 로 사용되는 것
'''
# # 사용자 함수를 정의
# def intorduce(name, address):       # call4() 유형으로 정의
#     return f"제 이름은 {name}이고, {address}에 삽니다."
# # 함수 1 사용 : input() > 파이썬 내장함수
# name = input("이름을 입력하세요 >>>")
# addrres = input("주소을 입력하세요 >>>")
#
# # 함수 1의 결과값을 함수 2인 사용자 함수의 argument로 사용 > 그 결과값을 함수 3인 print()함수의 argument로 사용
# print(intorduce(name,addrres))
'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현
돈을 넣으면 몇잔을 살 수 있는 지 그리고 잔돈은 얼마인지 
함수 정의 
- 반환값 : 없음
- 함수이름 : vending_machine()
- 매개변수 : 정수 money
코드 구성 
def vending_machine():
    # 함수 
vending_machine(3000)
ex)
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
# '''
# def vending_machine():
#     for _ in range(5):
#
#
# vending_machine(3000)
# money = 3000
# price = 700
# #charge = 3000 -(700 * drink)
# for i in range( int(money / price) + 1):
#     print(f"음료수 = {i}개, 잔돈 = {money - (price * i)}")

# return 타입 없으니 print()로 마무리 / 매개변수 명이 통제
# def vending_machine(money):
#     for i in range( money // 700 + 1 ):
#         print(f"음료수 = {i}개, 잔돈 = {money - (700 * i)}")
# vending_machine(3000)
'''
예제 구구단 출력하기 
함수 정의 :
함수 이름 : multiply
매개변수 : 정수 n

실행 예 
몇 단을 출력하시겠습니까? >>> 3 
# dan = 2
# while dan < 10:          값이 있으면 True로 취급
#     number = 1
#     while number < 10:
#         print(f" {dan} x {number} = {dan * number}")
#         number += 1
#     dan += 1
# '''
# A = int(input("몇 단을 출력하시겠습니까? >>>"))
# while A == A:
#     number = 1
#     while number < 10:
#         print(f" {A} x {number} = {A * number}")
#         number += 1

# def multiply(n):
#     for i in range(1, 10, 1):
#         print(f" {n} x {i} = {n*i}")
# dan = int(input("몇 단을 출력하시겠습니까? >>>"))

def multiply2():
    dan = int(input("몇 단을 출력하시겠습니까? >>>"))
    for i in range(1, 10, 1):
        print(f"{dan} x {i} = {dan*i}")
multiply2()
# print(dan)      # 오류 발생 > 함수를 정의만 하는 것은 사용 x, 변수에 해당하지 않음
# dan = 3         # 그리고 structure를 확인한 결과 선언한 dan x
# print(dan)
