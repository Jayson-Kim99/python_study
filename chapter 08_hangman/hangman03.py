import random # 특정 모듈을 사용한다는 것을 맨 처음 명시

'''
"".join(반복가능객체) method : . 앞에 있는 문자열을 기준으로 반복 가능 객체의
요소들을 합쳐서 str로 반환
'''
# temp = ["안","세","하","녕","요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print("".join(temp))

word_list = ["apple","banana","camel"]
chosen_word = random.choice(word_list)

print(chosen_word)

display = []
#todo - 1 : "_"가 적용된 display 구현
#todo - 2 : 사용자가 추측 반복을 위해 while 반복문 작성
# 사용자가 모든 문자열 맞췄을 경우 반복문 정지
# 반복문 종료후 print("정답입니다!!") 출력
for letter in chosen_word:
    display.append("_")
print(display)

while "_" in display:
    guess = input("알파벳을 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print("".join(display))
print("정답입니다!!")