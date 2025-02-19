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
'''

class Korean2:
    country = "대한민국"

    # 클래스 메서드 정의법
    @classmethod                            # < 명시하면 밑의 코드가 클래스 메서드로 작성
    def trip(cls, travelling_site):         # 첫번째 매개변수가 self X / cls O 자동완성
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

# 클래스 메서드의 호출
Korean2.trip("대한민국")
Korean2.trip("미국")
# 객체생성
man2 = Korean2
man2.trip("일본")
# 클래스 변수 때와 마찬가지로 객체명.클래스메서드명()으로 호출 가능
# 하지만 마찬가지로 얘가 인스턴스 메서드인지 클래스 메서드인지 구분 x
# 권장하지 않음