'''
1. 클래스 변수

    인스턴스 변수 : 인스턴스 마다 서로 다른 값을 지닌느 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근방식 - 인스턴스 접근(O)
                - 클래스 접근(X)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근방식 - 인스턴스 접근(O)
                - 클래스 접근(O)
'''
from itertools import count
from multiprocessing.pool import CLOSE
from pstats import add_func_stats

#
# # 클래스 변수 예제
# class Korean:
#     country = "한국"
#     # 인스턴스 변수의 경우 생성자 내부에 있었습니다. 클래스 변수의 경우에는 이상처럼
#     # 클래스 내부에 그냥 선언 및 초기화
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# # 객체생성
# man = Korean(name="안근수", age= 38, address= "부산")
# print(man.name)     # 객체의 속성 확인 방법
# print(man.age)      # 객체의 속성 확인 방법
# print(man.address)  # 객체의 속성 확인 방법 > 전부 인스턴스 변수 확인
#
# #클래스 변수 확인 방법
# print(man.country)      #객체명.클래스변수명 통한 접근 : 가능
# print(Korean.country)   #클래스명.클래스변수명 통한 접근 : 가능

# 객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 하지만 클래스 내부의 코드를
# 들여다 보기 전까지는 country라는 변수가 클래스 변수인지 인스턴스 변수인지 확인이
# 불가능하다는 문제가 있습니다
# 이상의 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명으로 참조하기 보다는
# 클래스명.클래스변수명을 통해서 참조하는 것이 바람직

'''
클래스 메서드 : 클래스 변수를 사용하느 메서드
# '''
#
# class Korean2:
#     country = "대한민국"
#
#     # 클래스 메서드 정의법
#     @classmethod                            # < 명시하면 밑의 코드가 클래스 메서드로 작성
#     def trip(cls, travelling_site):         # 첫번째 매개변수가 self X / cls O 자동완성
#         if cls.country == travelling_site:
#             print("국내 여행입니다.")
#         else:
#             print("해외 여행입니다.")
#
# # 클래스 메서드의 호출
# Korean2.trip("대한민국")
# Korean2.trip("미국")
# # 객체생성
# man2 = Korean2
# man2.trip("일본")
# 클래스 변수 때와 마찬가지로 객체명.클래스메서드명()으로 호출 가능
# 하지만 마찬가지로 얘가 인스턴스 메서드인지 클래스 메서드인지 구분 x
# 권장하지 않음
'''
2. 클래스 메서드
    : 클래스 변수를 사용하는 메서드
    
        특징 : 
            1) 인스턴스 또는 클래스로 호출 > 하지만 클래스 변수와 같이 클래스로 호출 하는 것을 권장
            2) 생성된 인스턴스가 없어도 호출가능 (클래스 호출)
            3) @classmethod 데코레이터(decorator)를 표시하고 작성
            4) 매개변수 self를 쓰지 않고 cls를 사용 > self는 객체를 의미하기 때문 (self는 인스턴스에 사용)
        
        호출방식 :
            클래스명.메서드명() > self를 사용하지 않기 때문에 '인스턴스'변수에 접근이 불가능
                cls를 통해 클래스 변수에만 접근가능

Korean2 클래스에서 정의된  trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작
첫 번째 매개변수는 cls는 class의 축약어 , 여기서는 클래스 Korean2를 의미함
따라서 cls.country 는 Korean2.country와 동일한 의미 이를 내부에서는 cls.country로 표기
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로도 호출가능 , Korean2.trip(argument)

3. 정적메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 > 즉 인스턴스 변수에 접근하여 사용하는 것이 불가능함
        - 클래스 메서드와의 공통점 #1 
        인스턴스를 생성하지 않아도 사용가능 > 클래스 메서드와 공통점 #2
        
    특징 : 
        1) 인스턴스 또는 클래스로 호출가능 > 클래스 메서드와 공통점 
        2) 생성된 인스턴스가 없어도 호출가능 > 클래스 메서드와 공통점 
        3) @staticmethod 데코레이터를 표기하고 작성  > 클래스 메서드와 차이점 #1
        4) 반드시 작성해야 할 매개변수(self,cls)없음 > 클래스 메서드와 차이점 #2
정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스 / 클래스  
'''

# class Korean3:
#     country = "한국"
#
#     @staticmethod
#     def slogan():
#         print("Imagine Your Korea!"
#
#     @staticmethod
#     def slogan2(str_example):
#         print("Imagine Your Korea!" + str_example)

'''
기본 예제 

가방을 만들 때마다 현재 만드러진 가방이 몇 개인지 계산 할 수 있는 Bag 클래스 정의
'''
#
# # 클래스 정의
# class Bag:
#
#     count = 0                   # 클래스 변수 선언 및 초기화
#
#     def __init__(self):         # 생성자 / 인스턴스 메서드에 해당함 > 아무@가 없음
#         Bag.count += 1          # 객체 하나 생성할 때마다 클래스 변수가 count 1 증가
#         print("가방이 생성되었습니다.")   # 인스턴스 메서드가 클래스 변수를 참조할 때는
#                                         # 클래스 명.클래스변수명
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1          # 클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count 가 아니라 cls. count
#
#     @classmethod
#     def remain_bag(cls):        # 클래스 변수를 main 단계에서 직접 참조하는 것이 보안상 좋지 않기 때문에
#         return  cls.count       # 클래스 메서드를 생성(getter형태로)하여 참조
#
# print(f"현재 가방 재고 : {Bag.count}")            # 클래스 변수를 직접 참조
# print(f"현재 가방 재고 : {Bag.remain_bag()}")     # 클래스 변수를 getter를 통해 메서드를 경유하여 참조
#
# # 객체 생성
# bag1 = Bag()    # 생성자 상기 해야함 아무 속성이 없기 때문에 argument를 채울 필요  X
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# bag1.sell()     # 인스턴스명.클래스메서드()로 호출 가능은 하지만 애매함
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# Bag.sell()      # 클래스명.클래스메서드명() 호출 > 권장하는 방싱

'''
이상의 코드를 보변 예시로써 적합하기 힘든ㅁ
인스턴스명.sell()로 작성한다면 특정한 가방 인스터스가 팔렸다고 볼 수 있기 때문에 가독성이 더 높은 반면 
Bag.sell()로 작성하게 된다면 어던 가방이 팔렸는지 모르고 그냥 가방 count 변수만 하나 줄었음

코딩 할 때 변수 / 메서드를 인스턴스 수준으로 작성 할 지 혹은 클래스 수준으로 작성할지 고민해야함

응용예제

1. 다음 지시를 읽고 이름과 전체 인구수를 저장할 수 있는 Person클래스 작성

지시사항

1. 다음과 같은 방법으로 man과 woman 인스턴스 생성 
man = Person("안근수")
woman = Person("안근순")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메세지를 출력
안근수(이)가 태어났습니다.
안근순(이)가 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회 할 수 있도록 작성
print(f"전체 인구수 : {Person.get_population()}")

4. 다음과 같은 방법 으로 man 인스턴스 삭제 
del man

삭제되면 
RIP 안근수
'''
#
# class Person:
#
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f"{self.name}(이)가 태어났습니다.")
#
#     # 소멸자 정의
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     def __del__(self):
#         Person.population -= 1      # 객체가 소멸되었을 때 전체 인구수가 줄어야 한다는 점을 고려
#         print(f"RIP{self.name}")    # 추가한게 -= 1 파트임
#
# man = Person("안근수")
# print(f"전체 인구수 : {Person.get_population()}")
# woman = Person("안근순")
# print(f"전체 인구수 : {Person.get_population()}")
# del man
# print(f"전체 인구수 : {Person.get_population()}")
# print("프로그램이 종료되었습니다.")
#

'''
클래스 변수 / 클래스 메서드 활용 예제

가게매출을 구한 Shop 클래스 작성

지시사항
1, Shop 클래스는 다음과 같은 변수가짐
    total : 가게 전체 매출액
    menu_list : {메뉴명 : 가격}으로 이루어진 딕셔너리 요소를 가지는 리스트
    
    menu_list = [{"떡볶이" : 3000}, {"순대" : 4000}, {"튀김" : 500}, {"김밥" : 2000}]
2, 매출이 생기면 다음과 같은 방식으로 판매량 작성
Shop.sales("떡볶이", 1)
Shop.sales("김밥", 2)
Shop.sales("튀김", 5)
3. 모든 매출을 작성한뒤 다음과 같은 방식으로 전체 매출액 작성
print(f"매출 : {Shop.get_total()}원")
'''

class Shop:

    total = 0
    menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]
    menus = {
        "떡볶이": 3000,
        "순대": 4000,
        "튀김": 500,
        "김밥": 2000
    }

    @classmethod
    def sales_2(cls, menu_key, account):
        # for key in cls.menus:
        #     if key == menu_key:
        if menu_key in cls.menus:
            cls.total += cls.menus[menu_key] * account

    @classmethod
    def sales(cls, menu_name, quantity):
        for menu_dict in cls.menu_list:
            if menu_name in menu_dict:      # menu_dict의 key들 중 menu_name에 해당하는 것이 있다면 의 조건문
                cls.total += menu_dict[menu_name]*quantity
                print(f"{menu_name}을(를) {quantity}개 판매")

    @classmethod
    def get_total(cls):
        return Shop.total


Shop.sales_2("떡볶이", 1)
Shop.sales_2("김밥", 2)
Shop.sales_2("튀김", 5)

print(f"매출 : {Shop.get_total()}원")
