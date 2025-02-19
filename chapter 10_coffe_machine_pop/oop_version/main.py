# from 파일명(소문자) import 클래스(대문자)
from idlelib.help import copy_strip
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# 외부파일에서 import 해온 class 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()} >>> ").lower()
    # todo - 1 : choice가 > off / report / 오타났을 때 작성하는 부분 완성하기
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:
            continue
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            # 위코드 정리
            # coffee_maker.is_resource_sufficient() 메서드를 확인해보면
            # drink,ingredients를 반복문 돌린다는 것 확인
            # 메서드가 어떤 자료형의 argument를 요구하는 지
            # continue가 실행되면 밑 코드라인은 실행되지 않고 while 반복문 앞으로 감
            # 재료가 충분한지 확인 > 돈 받기 > 받은 돈이 음료가격보다 높으면 > 음료 만들어준다
            # elif choice != menu.__init__(): # < 나혼자 했는데 이게 왜 돌아가지 임
            #     menu.find_drink(choice)