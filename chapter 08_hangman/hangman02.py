import random

word_list = ["apple","banana","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1 : 비어있는 list인 distplay를 마드시오
# chosen_word의 각 문자 개수마다 "_" 를 추가하시오 . ex choesen_word == "apple"이라명.
# display["_","_","_","_","_","_"]이 되어야 합니다 개수만큼 나오게

display = []

# # 일반 for문
# for _ in range(len(chosen_word)):
#     display.append("_")
# print(display)

# 향상된 for문
for letter in chosen_word:
    display.append("_")
print(display)

# todo - 2 :

guess = input("알파벳을 입력하세요 >>> ").lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
