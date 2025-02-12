'''
while 반복문
    while 다음에 나오는 조건문이 참이라면 이하의 실행문이 실행(조건문인 False가 될 때까지)
형식 :
while 조건문:
    실행문
'''
# num1 = 1
# while num1 > 0:
#     print(num1)

'''
그래서 while 반복문을 작성할 때 고려할 점
    특정상황에서 조건식이 False가 될 수 있도록 사전에 미리 지정
    > 아닐경우 무한루프에 빠짐 
'''
# num2 = 1
# while num2 < 11:
#     print(num2)
#     num2 += 1 # 특정 조건에서 False가 될 수 있도록 지정
'''
if문과 비교 : 
     if문의 경우 조건식이 참일 때 실행문이 한번 실행
     while문의 경우 조건식이 참일 때 실행문이 반복 실행
     특정 조건이 맞을 경우 아닌경우의 고민이 필요
'''
# num3 = 10
# while num3 > 0:
#      print(num3)
#      num3 -= 1
'''
중첩 while문(Nawsted while -loop) : while문 내부에 while문이 나타나는 것
ex) 
총 5일 동안 매일 3시간씩 수업을 진행합니다. 매일 '1일차 1교시입니다.'
1일차 부터 5일차 까지 반복 되는 일수와 1교시부터 3교시까지 반복되는 시간이라은 2개의 반복 처리 대상을 기준으로 중첩 while문을 작성
'''
# day = 1
# while day < 6:  5일차 까지 출력
#     hour = 1
#     while hour < 4:  3교시까지 반복 출력
#         print(f"{day}일차 {hour}교시 입니다.")
#         hour += 1
#     day += 1  들여쓰기 주의
'''
예제 
구구단 2단부터 9단
'''
# dan = 2
# while dan < 10:          값이 있으면 True로 취급
#     number = 1
#     while number < 10:
#         print(f" {dan} x {number} = {dan * number}")
#         number += 1
#     dan += 1
num1 = 1
while num1 < 101:
    print(f"{num1} {num1+1} {num1+2} {num1+3} {num1+4} {num1+5} {num1+6} {num1+7} {num1+8} {num1+9}")
    num1 += 10
# 위코드는 반복 10번 하는 경우
'''
n2 = 1
while n2 < 101:
    print(n2, end = "")
    if n2 % 10 == 0:
        print()
    n2 += 1
위코드는 숫자 끝마다 end 를 표시함 그래서 100(end)가 나옴 
'''