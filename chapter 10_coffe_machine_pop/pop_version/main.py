MENU = {
    "에스프레소" : {
        "재료" : {
            "물" :50,
            "커피" : 18,
        },
        "가격" : 1.5,
    },
    "라떼" : {
        "재료" : {
            "물" : 200,
            "우유" : 150,
            "커피" : 24,
        },
        "가격" : 2.5,
    },
    "카푸치노" : {
        "재료": {
            "물" : 250,
            "우유" : 100,
            "커피" : 24,
        },
        "가격" : 3.0,
    }
}

profit = 0
resources = {
    "물" : 300,
    "우유" : 200,
    "커피" : 100,
}

logo = '''
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |  _________   | || |  _________   | |
| |   .' ___  |  | || |     /  \     | || | |_   ___  |  | || | |_   ___  |  | |
| |  / .'   \_|  | || |    / /\ \    | || |   | |_  \_|  | || |   | |_  \_|  | |
| |  | |         | || |   / ____ \   | || |   |  _|      | || |   |  _|  _   | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |  _| |_       | || |  _| |___/ |  | |
| |   `._____.'  | || ||____|  |____|| || | |_____|      | || | |_________|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
'''
print(logo)

# print(MENU)
# print(MENU["라떼"]["재료"]["우유"])
# # 카푸치노의 가격을 콘솔에 출력
# # 에스프레소의 물 양을 콘솔
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])
# profit = 0
# resources = {
#     "물" : 300,
#     "우유" : 200,
#     "커피" : 100,
# }
# resources 에서 에스프레소 두잔을 뽑았을 때, 남는 물,우유,커피량을 연산하고,
# 그 결과를 콘솔에 출력하시오
# resources["물"]-= MENU["에스프레소"]["재료"]["물"]*2
# resources["커피"]-= MENU["에스프레소"]["재료"]["커피"]*2
# print([resources])
# 이상을 진행했을 때 커피 두잔이 자판기에서 나왔기 때문에 자판기에는 돈이 들어감
# 자판기에 profit 변수에 적절한 가격을 대입
# profit += MENU["에스프레소"]["가격"] *2
# print(profit)



#로고 (text to ascii art 사이트 )
#off 입력 시 입력하면 종료
#report 입력 시 resources와 profit을 참조 manual로 콘솔에 출력
#잘못 입력시 잘못 입력하셨습니다 안내문 출력

# choice가 "라떼"라는 str 데이터라면 , "라떼"를 만드는 데 필요한 재료를 조회하는 방법

# 함수 정의
def make_coffe(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU[음료이름][재료]들을 차감"""
    for item in order_ingredients:      #resources를 반복돌리지 않는 이유는 drink_name이 반복
        resources[item] -= order_ingredients[item]
    print(f"{drink_name}☕가 나왔습니다. 맛있게 드세요!")

def is_resources_enough(order_ingredients):
    """DocString : 함수 / 클래스 / 메서드가 어떤 작동하는지 사람들에게 설명하는 기능
    주문 받은 음료를 reosources에서 재료 차감을 하고 난 후 , 음료 만들기가 가능하면
    True 반환 , 아니면 False 반환
    : param : order_ingredients
    : return : True / False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이 부족합니다.")
            return False
        return True

def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수 call3()유형
    쿼터 , 다임, 니켈, 페니 네 종류의 동전
    쿼터 = 0.25달러
    다임 = 0.1달러
    니켈 = 0.05달러
    페니 = 0.01달러
    quarters, dimes, nickels, pennies"""
    # quarters = float(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    # dimes = float(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    # nickels = float(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    # pennies = float(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01
    # return quarters + dimes + nickels +pennies
    # 축약 버전
    total = 0.0
    total += float(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    total += float(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    total += float(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    total += float(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01

    return total
# 들어온 동전 금액과 가격을 비교하는 함수
def is_ransction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료가격을 매개변수로 받아
    동전이 가격보다 높으면 True / 아니면 False"""
    charge = money_received - drink_cost
    if charge >= 0:
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}를 반환합니다.")
        return True
    else:
        print(f"동전이 충분하지 않습니다. 금액${money_received}을 반환합니다.")
        return False

is_on = True

while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    # 만약에 초이스가 off라면 종료함
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"물 : {resources["물"]}ml\n우유 : {resources["우유"]}ml\n커피 : {resources["커피"]}g\n돈 : ${profit}")
    elif choice in ("에스프레소","라떼","카푸치노"):   # 에스프레소 / 라떼 / 카푸치노 중 하나를 입력했을 때 다음 단계로 넘어가는 부분
        # 자판기에 메뉴명을 정확히 입력했을 때
        # 1. 자원이 충분한지 확인해서 T / F
        # 2. T 라면 돈을 받아서 계산 ->  해당 금액의 가격보다 높은지 확인 -> T / F
        # 3. T 라면 음료를 만들어주는데, resources dict에 있는 수량 감소 / profit에 음료 가격만큼 + 시킴
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            money_received = process_coins()        # 함수 호출한 결과값을 변수에 대입
            if is_ransction_successful(money_received,drink["가격"]):
                make_coffe((choice),drink["재료"])
    else:
        print(f"잘못 입력하셨습니다. 다시 입력하세요. ")
