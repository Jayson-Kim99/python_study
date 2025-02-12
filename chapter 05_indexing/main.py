'''
문자열 indexing
print(type("안녕하세요"))를 실행했을 때.
<class 'str'>이라고 출력되는 것을 확인할 수 있습니다.
str = string의 줄임말 '줄'이란 의마
index = 문자열 (Collections - 추후 수업 예정)을 구성하는 모든 요소에 부여한 고유한 번호.
    시작하는 번호는 0 1이 아님
'''
#name = "aksdh"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
'''
마이너스 인덱스 : 문자열 뒤에서부터 부여하는 번호 마지막 문자의 번호는 -1 
'''
'''
문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 다어나
    문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 
    추출하는 방법
형식 :
a [시작인덱스 : 종료인덱스 : 증감값]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 변화(인덱스 넘버가 1씩증가 0,1,2...)
'''
#print(name[:2:]) # 종료 인덱스의 앞까지만 추출됨.
'''
기본 예제 
네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리를 출력하시오.
네자리 숫자를 입력하세요 >>> 2025
맨 마지막 숫자는 5입니다.
맨 마지가 숫자느 5이며, 홀수 입니다.
'''

# a = input("네 자리 숫자를 입력하세요 >>>")
# 형변환을 조건문에 삽입하여 그대로 사용함
# if int(a) % 2 == 0:
#     print(f"맨 마지막 숫자는 {a[3]}이며, 짝수 입니다")
# else:
#      print(f"맨 마지막 숫자는 {a[3]}이며, 홀수 입니다")

# 변수를 선언해서 활용
# last_num = int(a[3])
# if last_num % 2 == 0:
#     even_odd = "짝수"
# else:
#     even_odd = "홀수"
# print(f"맨 마지막 숫자는 {last_num}이며 {even_odd}입니다.")

# 마이너스 인덱스를 활용

# last_num = int(a[-1])
# if last_num % 2 == 0:
#     even_odd = "짝수"
# else:
#     even_odd = "홀수"
# print(f"맨 마지막 숫자는 {last_num}이며 {even_odd}입니다.")
'''
응용 예제

미세먼지 저감 활동의 일환으로 차량2부제를 실시하고자 합니다. 사용자로부터 차량 번호를 입력바다
짝수로 끝나면 '운행가능' , 아니면 '운행불가'가 출력되는 프로그램을 작성하시오
단, 번호는 '237가1234'와 같은 형식으로 입력 받는다고 가정합니다.

실행 예
차량 번호르 입력하세요 >>> 237가 1234
차량번호 237가 1234는 오늘 운행 가능합니다.
'''

# a = input("차량번호를 입력하세요 >>>")
# car_num = a
# last_num = int(a[-1])
# if last_num % 2 == 0:
#     even_odd = "운행가능"
# else:
#     even_odd = "운행불가"
# print(f"차량번호 {car_num}는 오늘 {even_odd}입니다.")





























