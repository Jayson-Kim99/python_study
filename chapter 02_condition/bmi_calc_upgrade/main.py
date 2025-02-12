logo = """
 ____  __  __  ____ 
(  _ \(  \/  )(_  _)
 ) _ < )    (  _)(_ 
(____/(_/\/\_)(____)
"""
print(logo)
height = float(input("당신의 키는 몇 cm입니까? >>>")) / 100
weghit = float(input("당신의 몸무게는 몇 kg입니까? >>>"))
bmi = round(weghit/(height**2),2) # 반복적으로 나오는 경우 변수에 대입하면 가독성 +
if bmi <= 18.5:
    print(f"당신의 bmi지수는 {bmi}이고,저체중입니다.")
elif bmi <= 23:
    print(f"당신의 bmi지수는 {bmi}이고,정상입니다.")
elif bmi <= 25:
    print(f"당신의 bmi지수는 {bmi}이고,과체중입니다.")
else:
    print(f"당신의 bmi지수는 {bmi}이고,비만입니다.")
