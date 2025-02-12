'''
지시사항
사용자에게 전체 음식값($) 몇 % 의 팁을 낼 것인지, 인원수를 입력 받을 예정

음식 가격은 얼마 입니까? >>> $200
몇 퍼센트(%)의 팁을 내실 예정입니까, 10,12,15% 중에서 선택하세요 >>> 10
몇 명의 인원이 나누어 내나요? >>> 5
당신이 내야할 전체 음식 금액은 $44.0달러입니다.
'''
# food = float(input("음식 가격은 얼마입니까? >>>$ "))
# percent = float(input("몇 퍼센트(%)의 팁을 내실 예정입니까, 10,12,15% 중에서 선택하세요. >>>"))
# people = int(input("몇 명의 인원이 나누어 내나요? >>>"))
# percent = percent / 100
# tip = food * percent
# total_price = food + tip
# price_per_person = total_price / people
# price_per_person = round(price_per_person,2)
# print(f"당신이 내야할 전체 음식 금액은 {price_per_person}달러입니다.")
food = float(input("음식 가격은 얼마입니까? >>>$ "))
percent = float(input("몇 퍼센트(%)의 팁을 내실 예정입니까, 10,12,15% 중에서 선택하세요. >>>")) /100
people = int(input("몇 명의 인원이 나누어 내나요? >>>"))
print(f"당신이 내야할 전체 금액은 ${round(food * (1+percent) / people,2)}입니다.")
print(f"당신이 내야할 전체 금액은 ${((food * (1+percent)) / people) :.2f}입니다.")
#23번 라인 경우 어떤 상황에서도 소수점 둘째자리까지 표기 