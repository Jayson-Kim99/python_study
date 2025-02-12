'''
1. if문
    if문은 조건이 참(true)일 때만 해당 블록의 코드를 실행합니다.
'''
# age = 20
# if age >= 19:
#     print("성인입니다.")     # True 일 때만 실행
'''
if문에서 주의할 점 :
    1) if와 같은 라인에 작성된 코드는 True / False으로 구분할 수 있어야만 함.
    2) if와 같은 라인에 있는 조건문이 끝났을 때 콜론(:)으로 마무리
    3) python에서는 타 언어들과 달리 들여쓰기(indentedf writing)이 '매우' 중요
'''
# age = 3
# if age >= 19:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")
'''
3. if - elif - else 
여러조건을 동시 검사
'''
# age = 14
# if age >= 19:
#     print("성인입니다.")
# elif age >= 8:
#     print("학생입니다.")
# else:
#     print("아동입니다.")
'''
    이상의 코드에서 확인 할 수 있는 점 
    1) 첫 번째 조건은 Flase이지만
    2) 두 번째 조건은 True이므로 elif문 실행
    3) 이후 조건은 else 실행 종료
    if 조건문의 전체 형식 :
if 조건식 1 : 
    실행문1
(elif 조건식 2:)
    (실행문 2)
(elif 조건식 3:)
    (실행문 3)
else:
    실행문 4
'''
# age = 3333
# has_ticket = True
# if age >= 20:
#     if has_ticket:
#         print("영화관 입장이 가능합니다.")
#     else:
#         print("티켓을 구매하세요.")
# else:
#     print("미성년자는 출입할 수 없습니다.")
'''
5. 조건문에서 자주 쓰이는 연산자
    비교 연산자 : 
        1) == 같다 
        2) != 같지 않다
        3) > 초과
        4) < 미만
        5) >= 이상
        6) <= 이하
    논리 연산자 : 
    1) and : A and B -> A 와 B가 모두 참일 때 실행문 실행
    2) or : A or B -> A 혹은 B 중에 하나가 참이면 실행문 실행 
    3) not : if not A -> A가 false일 때 실행문 실행
'''
age = 25
has_ticket = True
if age >= 19 and has_ticket:
    print("영화관 입장이 가능합니다")
else:
    print("입장할 수 없습니다.")