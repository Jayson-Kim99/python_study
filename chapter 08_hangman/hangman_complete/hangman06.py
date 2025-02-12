# import 다른 파이썬 파일 명을 쓰면 현재 파일에서 쓸 수 있음
# 사용 할 때는 파일명.
import random
import hangman_word_list
import hangman_arts

end_of_game = False
lives = 6
chosen_word = random.choice(hangman_word_list.word_list)
display = []

for letter in chosen_word:
    display.append("_")

print(hangman_arts.logo)
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
    print(hangman_arts.stages[lives])
