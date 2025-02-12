import random
from hangman_arts import logo, stages
from hangman_word_list import word_list
'''
import 문 학습
    import문 을 단독으로 쓸 경우에는 모듈명.변수명 혹은 모듈명.메서드명() 명시
    ex 
    모듈명.메서드명() > random.choice()
    모듈명.변수명 > hangman_arts.logo 
import 응용
    from - import문을 쓰게 될 경우 모듈명 생략
    from - import의 경우
    from a import * 로 작성 : a 모듈 내에 있는 모든 변수 참조
    *(asterisk) : all 의미
    다만 너무 많은 부분을 from - import 구문 작성시 
    특정 변수가 해당 파일에서 자체 생성 혹은 어떤 파일들에서 참조 되었는지 가시적으로 확인x 제한 사용
    from a import a, b, c 의 경우 그나마 괜찮
    * 개념과 함쳐진 경우 가독성 매우 떨어짐
    마찬가지로
    from random import choice의 경우 해당 메서드 1개만 참조 했기에 문제 x
    from random import * 로 작성 경우 가독성 문제가 야기 될 수 있음 
'''
end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display.append("_")

print(logo)
while not end_of_game:

    guess = input("알파벳 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True
            print(f"정답은 {chosen_word}입니다.")

    if "_" not in display:
        print("정답입니다:)")
        end_of_game = True

    print(" ".join(display))
    print(stages[lives])
