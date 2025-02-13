'''
1. 클래스 도입의 필요성
'''

# 매개변수가 6개인 함수를 하나 정의
#
# def student_info(name,department,professor,phone,address,grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)
#
# name1 = "김일"
# department1 = "**과"
# professor1 = "noll"
# phone1 = "010-1111-1111"
# address1 = "지역"
# grade1 = "A"
# student_info(name1,department1,professor1,phone1,address1,grade1)

'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수 처리
하지만 만들어야 할 변수의 개수가 많고, 학생 한 명당 매개변수가 6개라면 ,학생 100명일 경우 600개의 변수처리 
'''

# student_info(grade = "B",
#              address= "서울",
#              phone="010-1234-5678",
#              professor="john",
#              department="computer",
#              name="김이"
#              )                      # keyword argument

#name2 ,~~ ,grade2 라는 변수를 선언 거기에 내 정보 입력후
# student_info 출력
#
# name2 = "김삼"
# department2 = "기계설계과"
# professor2 = "jay"
# phone2 = "010-4011-7160"
# address2 = "부산시"
# grade2 = "A"
#
# student_info(name = name2,
#              department = department2,
#              professor = professor2,
#              phone = phone2,
#              address = address2,
#              grade = grade2
#              )
'''

이상의 상황들(변수에 각각 데이터를 대입한 후 함수의 argument로 사용하거나, 혹은 데이터를 직접 argument에 등록)을 
벗어나기 위해서 클래스와 객체 개념

class = 객체를 만드는 도구 - 설계도 / 틀 / 청사진
    
    자옫차 설계도 > 클래스
    설계도를 통해 생성된 자동차들 > 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있음
    마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있음
    
    인스턴스(instance) 역시 클래스를 이용해서 생성된 객체를 가리키는 용어
    객체와 인스턴스는 그 둘을 바라 보는 관점의 차이로 불 수 있음 
    1. '자동차 설계도'로 만든 자동차는 객체(object)
    2. 자동차는 자동차 설계도의 인스턴스(instance)

1. 클래스 정의
    클래스를 작성한 것을 클래스 정의라고 합니다 > 함수 정의
형식:

class 클래스명(대문자로 시작):
    본문
--------------------------
객체생성형식 :                 > 함수 호출 과 비슷한 느낌

객체이름 = 클래스명()

'''
# 클래스 정의 형식 ex
class WaffleMachine:        # 클래스 명은 대문자로 시작, Pascal Case로 표기함 . python에서는 변수는  snake_case
    pass                    # 나중에 코드 작성하겠다는 의미 실행시 오류발생 x

# 객체생성예시
waffle = WaffleMachine()    # 소괄호() 중요
print(waffle)

'''
print(waffle)을 실행 시켰을 때 <__main__.WaffleMachine object at 0x0000026170A7E240>에서 object라고 
표기한 점을 미루어 waffle은 WaffleMachine 의 객체

클래스 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소 지님
    객체를 생성하기 위해서는 클래서는 객체가 가져야 할 '값' 과 '기능' 필요
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 구분 
        1) 클래스 변수 : 클래스를 기반을 생성된 모든 인스턴스들이 공유하는 변수
        2) 인스턴스 변수 : 인스턴스 들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
        
    인스턴스 변수 : 클래스를 기반을 만들어지는 모든 인스턴스들이 각각 따로 저장하는변수 
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙임
        인스턴스 메서드는 첫 번째 매개변수로 self를 추가 해야함
        
'''