'''
1. for  반복문의 기본 개념 :
     정해진 구간 혹은 집합 내의 요소들으 순서대로 꺼내면서 반복 작업 수횅.
     예를 들어 문자열의 index 개념
     string의 경우 문자열의 문자 개수만큼 반복이 진행
     Collection을 기반으로 반복 가능 다음시간에 할 예정
        1) 숫자 범위 이용
        range() : 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 연계
'''
# 1부터 10까지를 출력하는 for 반복문
# n = 1
# for i in range(11):         # 현재 상황에서의 반복 횟수는 11
#     print(i)
#
#
# for i in range(10):         #반복횟수 10, 중요한 것은 시작지점이 0부터라는 점
#     print(i+1)
'''
range() 함수의 응용 :
    range((시작값,) 종료값,(증감값))
    시작값 : 생략가능, 생략할 경우에 0부터 시작
    종료값 : 명시하지 않으면 끝까지 진행
    증감값 : 생략 가능, 생략할 경우에 1씩 증가 -> index에서 slicing 개념과 비슷
for 반복문
형식 : 
for i in range(시작값,종료값,증감값,):
    반복문실행
'''
# for i in range(1,10,1):     #종료값 10인데 1부터 시작해도 9까지 나옴
#     print(i)                #종료값 바로 앞까지 출력이 이루어짐 확인 할 수 있습니다.
'''
2) 문자열 반복
    문자열의 경우 []를 통해 내부에 인덱스 넘버를 명시할 수 있다는 것
    in range()를 사용하는 방법 및 향상된 for문을 사용하는 방법을 통해 
    문자를 하나씩 추출 가능
'''
name = "askdfasdfasdf"
# #1) in range()를 이용하여 문자르 추출하는 방법
# for i in range(len(name)):      #len() : () 안에 들어가는 요소의 길이를 변환하는 함수
#     print(name[i])
#2) enhanced for loop를 통한 방식
for letter in name:         #name이라는 string에서 각 문자 하나씩을 뽑아 letter에 대입
    print(letter)
'''
대부분의 경우 반복문을 사용하게 되면 반복대상이 되는 객체는 복수형의 변수명을 지님
ex) numbers = [1,2,3,4,5,6]
for number in numbers:
    print(number)
향상된 for loop의 형식 :
for 변수 in 반복대상객체:
    반복실행문
반복대상객체(iterable) : 내부에 요소가 다수 들어가 있어 반복적으로 요소의 데이터를 다룰 수 있는 객체
    ex)  str, list, tuple, set, dict 
주의 사항 :
    if 조건문과 같이 들여쓰기가 매우 중요함 
문자열에서 특정 문자의 개수 세기
'''
# count_a = 0
# count_letters = 1
# for a in "banana":
#     if a == "a":
#         count_a += 1
#         print(a)
#         count_letters += 1
# print(f"a의 개수 : {count_a}")
# print(f"전체 문자 개수 : {count_letters}")
# print(f"전체 문자 개수 : {len("banana")}")
'''
reeborg's world hurdle # 1
for _ in range(6):
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
def turn_right():
    for _ in range(3):
        turn_left()
        
for _ in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def turn_right():
    for _ in range(3):
        turn_left()
        
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    jump()
hurdle # 3 
def turn_right():
    for _ in range(3):
        turn_left()
        
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
# maze 를 통과하는 우수법 코드 적용 사례
def turn_right():
    for _ in range(3):
        turn_left()            
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and wall_on_right():
        move()
    elif (right_is_clear() and front_is_clear()) or (wall_in_front() and right_is_clear()):
        turn_right()
        move()                              
'''
