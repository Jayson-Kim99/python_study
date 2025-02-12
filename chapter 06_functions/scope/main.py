'''
Scope : 범위
지역 변수 : 함수 내에 정의된 변수
전역 변수 : 함수 외부(main단계)에 정의된 변수
'''
# enemies = 1     # 전역 변수
# def increase_enemies():  # 함수 정의 시작
#     enemies = 2          # 같은 이름이지만 지역변수
#     print(f"함수 내부의 적의 숫자는 {enemies}입니다.")
# increase_enemies()       # 함수 호출
# print(f"함수 외부의 적의 숫자는 {enemies}입니다.")
# 지역 변수 = / = 전역 변수 > 변수명을 서로 다르게 하는 것이 혼란을 피하기 좋음

# # 함수 정의
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# # print(potion_strength)
# drink_potion()
#print(potion_strength)
# 지역 병수가 선언 되고 이를 호출 = x 함수 내에 있는 변수가 전역에서 참조 하는 것 x
'''
Global Scope
'''
# player_health = 10
# # 함수 정의
# def game():             # 함수 내부에 함수 정의 > jump 내에 turn_right 함수 사용
#     def drink_potion(): # 얘는 정의된 함수를 내에서 호출, 여기서는 함수 내에 정의를 새로함
#         #player_health += 2    # 마찬가지로 전역에서 선언되고 초기화된 변수를 함수 내에서 조작하는 것은 불가능
# #근데 무조건은 아님
#         global player_health # global을 선언하고 값을 바꿀 전역 변수 명을 쓰면 함수 내에서 전역 변수의 값 바뀜
#         player_health += 2
#     # 생길 수 있는 문제점 :
#     # 함수 호출 횟수에 따라 전역 변수 값 바뀜
#     # 전역 변수의 값을 정확히 알기 위해서 함수 호출 횟수를 알아야함
#     # 이상의 이유로 이런 코딩 방식을 선호되지 않음
#     drink_potion()
# game()
# print(f"체력은 {player_health}입니다.")
game_Level = 3
def create_enemy():
    enemies = ["좀비", "스켈레톤", "에일리언"]
    if game_Level < 5:
        new_enmey = enemies[0]

    print(new_enmey)
create_enemy()
'''
이상의 코드에서 생기는 문제
1. game_Level 이라는 전역변수를 create_enemy()라는 함수의 정의 부분에서 사용해도 오류 발생 x
2. 함수 정의 내부에서 if절에서 new_enemy라는 변수를 선언 및 초기화 했음
    if절 바깥에서 (들여쓰기 참조) new_enemy를 참조 했음에도 오류 발생 x
    1.의 이유 : game_Level이라는 전역변수의 값 바꾸는게 아님 , 참조만 해서 True/False만 반환하기 때문에 
        오류 발생하지 않음.
    2.의 이유 : if/while/for 같이 콜론을 기준으로 들여쓰기가 있는 모든 코드 블록들은
        지역 변수를 만드는 것으로 간주하지 않음 > 지역 변수의 용어 정의에 주목 
'''





































