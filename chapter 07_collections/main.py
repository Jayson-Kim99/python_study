'''
컬렉션(collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나 하나를 줄(str)로 묶어서 문자열로 출력하는데.
ex) '다수의 다른 string을 관리하는 방법은 무엇일까'에 관한 답
여러 명의 프로필을 관리한다고 가정해보겠습니다.
'''
from doctest import set_unittest_reportflags

# ahngeunsu = "이름 : 안근수\n나이 : 38\n직업 : 파이썬 강사"
# print(ahngeunsu)
# kimrandom = "이름 : 김랜덤\n나이 : 20 \n직업 : 학생"
# print(kimrandom)
'''
한 명 저장하는 데에는 문제가 없을 수 있음 매번 변수 하나에 이름, 나이 , 직업 등을 한 명 추가할 때마다 
정리하는 것은 비효율 직업만 조회하고 싶어서 전체 정보 확인 해야함
주소를 추가한다고 가정시 각변수를 모두 참조 > 수정 
한번에 관리하기 위해 컬렉션 사용
종류 : 
    1. list : 추가 / 수정 / 삭제가 언제나 가능 / a = [1,2,3] 대괄호 사용
    2. tuple : 추가 / 수정 / 삭제가 불가능 / a = (1,2,3) 소괄호 사용
    3. set : 중복된 값의 저장이 불가능 / a = {1,2,3} 중괄호 사용
    4. dict : 키 + 값으로 관리 / a {"name" : "안근수", "age" : 38} 중괄호 사용
1. list
     여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능
     하나의 배열(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형만을 저장할 수 있는 C,Java에 비해 
     python이 가지는 장점
'''
# li = [1,2,3,"김재우"]
# print(li)
'''
1-1 : list의 index와 slice
    list는 str과 동일한 방식의 index와slicing을 지원함
    1) 인덱스와 마이너스 인덱스
'''
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[-1])
# print(li[-2])
# print(li[-3])
# print(li[-4])
'''
2) slice
    str의 슬라이싱과 같이'시작인덱스 : 종료인덱스 : 증감값'을 이루어짐
'''
# list_num1 = [100,3.14,"hello"]
# list_num2 = list([4,5,6,7,8,9])
# print(list_num1)
# print(list_num2[0:4:2])
'''
3) list 요소의 추가 , 삭제
    list에 새로운 요소를 추가할 때는 .append()와 .insert()'메서드'를 사용할 수 있습니다
    기존 요소를 삭제할 때는 .pop() 메서드를 사용합니다
    .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
    .insert(위치,값) - 정해진 위치에 해당하는 값을 추가하는 메서드
# '''
# scores = [30,40,50]     # scores list 내에 있는 int 데이터인 30,40,50 을 요소(element)
# print(scores)
# scores.append(100)      # 함수와 달리 list명.메서드(데이터)의 형태로 사용
# print(scores)
# scores.insert(0, 90)
# print(scores)
'''
.pop() : 빈 괄호로 사용하면 맨 마지막 요소가 삭제
.pop(인덱스넘버) : 해당 인덱스의 요소 삭제 
'''
# scores.pop()
# print(scores)
# scores.pop(0)       # 오버로딩의 기초개념이 포함 동일한 메서드 명인데도 argument가 있을 수도 없을 수도 있음
# print(scores)
'''
교재에 없는 삭제 메서드 : .remove(값)을 사용하면 list내에 해당 값을 찾아 삭제함.
'''
# scores.remove(40)
# print(scores)
# 이상의 코드 를 실행 시킬 시 인덱스가 2개 밖에 없음 10개 element 추가함
# for i in range(10):
#     scores.append(i*10)
# print(scores)
# list 내의 요소를 하나씩 뽑아 내는 반복문 - for문 위 코드를 기준으로 뽑아내는 반복문
# for i in range(len(scores)):
#     print(scores[i])
# print()
# 향상된 for 문 사용
# for score in scores:        # collections의 경우 복수로 이름 짓고
#     print(score)            # 향상된 for문에서 각 변수는 단수로 이름 짓기
'''
2. tuple() : 저장된 값을 변경할 수 없는 list 
    인덱스와 슬라이스를 사용하지만 저장된 값 이외에는 추가 / 수정 / 삭제 불가능
    튜플은 소괄호 통해 생성
'''
# tuple_num1 = (1,2,3)
# tuple_num2 = tuple((4,5,6))
# tuple_num3 = 7, 8, 9
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
# 복수의 변수 선언 및 초기화 방법
# a, b, c = 7, 8, 9
# print(a)
# print(b)
# print(c)
'''
튜플 생성 방법  3을 이용 한다고 가정 값이 하나밖에 없는 튜플 생성시
tuple_num4 = 0 이라고 입력할 경우 생길수 있는 문제 
'''
# tuple_num4 = 0
# print(tuple_num4)
'''
1) 튜플에서의 인덱스 / 마이너스 인덱스
'''
# tuple_num6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(tuple_num6[2])    #collections의 element에서 type() 함수를 적용
#                         #element의 자료형이 반환
#                         #즉 , tuple_num6[2]는 3이라는 element르 가리킴
#                         #type 적용시 <class 'int'>로 출력
# tuple_num7 = "hello" , "nice to meet you" , "my name is" , "kim jaewoo" , "I am ", "26", "years old."
# for words in tuple_num7:       #str의 메서드.upper는 str을 대문자로 바꿔줌
#     print(words.title(),end=" ")
# print()
# for words in tuple_num7:       #words.title()을 적용하면 tuple 내의 element들이 전부 값이 바뀐 것이 아님
#     print(words,end=" ")       #words.title() 작성 시에만 적용
'''
3. set
    수학의 집합 개념을 구현한 자료형 .list와 차이점은 순서가 없음 인덱스 및 슬라싱 불가능 중복값 저장 불가능
    이를 활용하여 중복 제거용 사용, 교집합, 합집합, 차집합 같은 집합 개념이 필요한 경우 사용 
    set 사용시 {} 중괄호 사용
'''
# set_num1 = {1,2,3}
# set_num2 = set({4,5,6})
# print(set_num1)
# print(set_num2)
# # 비어 있는  list, tuple, set 생성
# li = []
# tu = ()
# se = {}
# print(type(li)) #<class 'list'>
# print(type(tu)) #<class 'tuple'>
# print(type(se)) #<class 'dict'>
'''
    se = {} 형태로 비어있는 set를 생성한 경우 se는 사실 <class dict>
    비어있는 set을 만들기 위해서는 세트 생성방법 2를 사용해야함
# '''
# se2 = set({})
# print(type(se2))
'''
특징 :
    1. 저장되는 순서 x > 인덱싱 / 슬라이싱 불가능
    2. 중복값 저장 x
    3. 특히 2.의 특징으로 set은 단독사용보다 list와 연계사용 많음
'''
# list_num5 = [1, 1, 2, 2, 3, 3, 3, 3]
# print(list_num5)
# set_num5 =set(list_num5) # 형변환 함수인 set()을 사용하고 list를 argument로 넣어 list > set
#
# print(set_num5)
# list_num6 = list(set_num5)
# print(list_num6)        # list로 형변환 후 슬라이싱, 인덱싱 사용가능
'''
set에는 인덱싱/ 마이너스 인덱싱/ 슬라이싱을 지원x 특정요소 추출을 위해 형변환 구조 list() 필요

    요소 관련 메서드
        .add() - set에 새로운 요소 추가
        .remove() - 기존요소 삭제
        .discard() - 기존요소 삭제
'''
# set_num6 = {10, 20, 30}
# set_num6.add(50)
# print(set_num6)
# set_num6.remove(50)
# print(set_num6)
# set_num6.discard(70)
# print(set_num6)
'''
4. dictionary - 사전
    flower - 꽃
    등으로 사전적 의미를 가짐 즉 ":" 을 기준으로 좌축과 우측이 나누어진 형태
    딕셔너리는 리스트 , 튜플, 세트와 달리 
    key - value의 구성으로 이루어짐
'''
# dict_num1 = {
#     "이름" : "김재우",
#     "나이" : 26,
#     "주소" : "부산광역시",
# }
'''
맨 마지막 ','의 의미는 혹시 후에 key-value를 추가할 때 이전 라인에서 콤마를 입력하고 
또 key : value 형태로 작성하기 귀찮으니 미리 쉼표를 찍어 쉽게 추가할 수 있도록 하는게 매너
'''
'''
    딕셔너리는 인덱스는 존재 x 위와 같이 key를 인덱스와 유사하게 사용
    즉, key 값을 알면 저장된 갑(value)를 확인 할 수 있는 구조.
'''
# list의 각 요소를 추출하는 반복문
# li2 = [10, 20, 30, 40]
# for num in li2:
#     print(num)
# # dictionary에서 같은 방식의 반복문
# for key in dict_num1:
#     print(key)              #그냥 print()하게 되면 dict_num1의 key만 추출
#     print(dict_num1[key])   #value를 추룰 하려고 하면 < 코드 라인과 같이 작성
#     print()
# # key 목록을 추출하는 메서드
# print(dict_num1.keys())
# print(dict_num1.values())
#
# print(type(dict_num1.keys()))   #<class 'dict_keys'>
# print(type(dict_num1.values())) #<class 'dict_keys'>
#
# keys = list(dict_num1.keys())
# values = list(dict_num1.values()) # index를 활용시 list로 형변환 필요
#
# print(keys)
# print(values)
#
# print(keys[1])
# print(values[1])

'''
1) 딕셔너리 요소의 추가 삭제
# '''
# dict_num1["직업"] = "코리아it아카데미 파이썬 강사"
# print(dict_num1)
# dict_num1["직업"] = "코리아it아카데미 웹 개발 강사"
# print(dict_num1)
# # key 하나당 하나의 value만 저장 가능
# # 삭제방법
# dict_num1.pop("직업")    #key를 정확하게 입력해야함
# print(dict_num1)        #key를 삭제하면 value를 같이 삭제
'''
응용 ex 
list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 부터 7번째 까지 추출한 결과 
그리고 그 list에서 2번째 요소를 출력하는 프로그램
'''
# list_origin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list_origin3 = list_origin[2:7]
# list_origin4 = list_origin3[1]
# print(f"3 번째 요소부터 7 번째 요소 = {list_origin3}")
# print(f"3 번째 요소부터 7 번째 요소 중 2 번째 요소 = {list_origin4}")
#
# # 반복적 사용을 하지 않을 경우
# list_origin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(f"3 번째 요소부터 7 번째 요소 = {list_origin[2:7:1]}")
# print(f"3 번째 요소부터 7 번째 요소 중 2 번째 요소 = {list_origin[2:7:1][1]}") # ★ 이런 표현을 사용 할 수 있어야 함 ★
'''
사용자로 부터 1에서 12월을 입력 받아 해달월이 며칠까지 있는지 출력하는 프로그램을 작성
실행 예
1 ~ 12 사이의 월을 입력하세요>>> 2 
2월은 28일까지입니다 
'''
# mouth = input("1 ~ 12 사이의 월을 입력하세요 >>> ")
# mouth_int = int(mouth)
# # last_dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # print(f"{mouth_int}월은 {last_dates[mouth_int-1]}")
#
# last_date_dict ={
# "1" : 31,
# "2" : 28,
# "3" : 31,
# "4" : 30,
# "5" : 31,
# "6" : 30,
# "7" : 31,
# "8" : 31,
# "9" : 30,
# "10" : 31,
# "11" : 30,
# "12" : 31,
# }
#
#
# last_dates_short = [28, 30, 31]
#
# if mouth_int == 2 :
#     last_date = last_dates_short[0]
# elif mouth_int in (4,6,9,11):
#     last_date = last_dates_short[1]
# elif mouth_int in ( 1, 3, 5, 7, 8, 10, 12):     # in 뒤에 collection 중에 하나 오면 됨 (),[],{} 가능
#     last_date = last_dates_short[2]
# else:
#     print("잘못입력하셨습니다.")
#     last_date = "X"
# print(f"{mouth}월은 {last_date}일까지 있습니다.")

'''
수학여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장 함
3명으로 가정하고 실행을 
ex 
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# s = int(input("학생 수 >>>"))
# r = []
# for i in range(s):
#     h = str(input("희망하는 수학여행지를 입력하세요 >>> "))
#     r.append(h)
# r = set(r)
# print(f"조사된 수학여행지는 {r}입니다.")
# r = list(r)
# print(f"조사된 수학여행지는 {r}입니다.")
'''
짝수만 추출하기
사용자에게 임의의 양을 정수를 입력 받으면 그정수만큼 숫자를 입력 받아  list에 저장
이후 저장된 숫자중 짝수만 새로운 list에 저장하여 출력하는 프로그램
ex
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [5,10,15,20,25,30]
입력 받은 숫자들 중 짝수는 [10,20,30]입니다
# '''
# s = int(input("몇 개의 숫자를 입력할까요? >>> "))
# r = []
# r1 = []
# for i in range(1,s+1):
#     h = int(input(f"{i}번째 숫자를 입력하세요 >>> "))
#     r.append(h)
#     h1 = h
#     if h1 % 2== 0:
#         r1.append(h1)
# print(f"입력 받은 숫자는 {r}")
# print(f"입력 받은 숫자들 중 짝수는 {r1}입니다.")

# 압축한 풀이
#
# a = []
# b = []
# for i in range(int(input("몇 개의 숫자를 입력할까요? >>> "))):
#     n2 = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     a.append(n2)
#     if n2 % 2 == 0:
#         b.append(n2)
# print(f"입력 받은 숫자는 {a}")
# print(f"입력 받은 숫자들 중 짝수는 {b}입니다.")
'''
딕셔너리 기반 연락처 관리
사용자로 부터 3명의 이름과 전화번호를 입력받아 딕셔너리에 저장한 뒤 , 입력한 정보를 추출하는 프로그램을 작성
ex
1 번째 사람의 이름을 입력하세요 >>> 김일 
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름을 입력하세요 >>> 김이 
2 번째 사람의 연락처를 입력하세요 >>> 010-5678-1234
3 번째 사람의 이름을 입력하세요 >>> 김삼 
3 번째 사람의 연락처를 입력하세요 >>> 010-9876-5432
입력 받은 연락처는 {'김일','010-1234-5678','김이'}
'''
# d = {}
# for i in range(3):
#     p = input(f"{i+1}번째 사람의 이름을 입력하세요 >>> ")
#     n = input(f"{i+1}번째 사람의 연락처를 입력하세요 >>> ")
#     d[p] = n
# print(f"입력받은 연락처는 {d}")
'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자 추가
문제 : 비어있는 list01 을 선언 그 안에 입력받은 횟수만큼 숫자를 추가
함수 정의 : add_numbers()
매개변수 : 정수 n

함수 호출 
add_numbers(last_num)

ex
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
# '''
# def add_numbers(n):
#     list01 = []
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
#
# def add_numbers2(n):
#     list02 = []
#     for i in range(n):
#         list02.append(i+1)
#     return list02

'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수
정의
이름 : count_even_odd
매개변수 : list numbers(요소는 정수)
함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개

'''

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"짝수의 개수 : {even_count}\n홀수의 개수 : {odd_count}")
count_even_odd([1,2,3,4,5,6,7,8,9,10])



