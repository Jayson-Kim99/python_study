'''
과제
은행 계좌를 관리하는 BankAccount 클래스 작성 이 클래스는 계좌 소유자 이름, 계좌 번화, 잔액을 인스턴스 변수로 가짐

지시사항
    1. BankAccount 클래스 정의 생성자 통행 owner, account_num. balance를 초기화
    2. 각 인스턴스 변수에 setter / getter 정의
    3. 입금 기능을 하는 인스턴스 메서드 (deposit())르 구현 > 입금 금액을 입력 받아 잔액 증가
        입금 금액이 0원 이하 입금 불가 로직
    4. 출금 기능을 하는 인스턴스 메서드 (withdraw())르 구현 > 출금 금액을 입력 받아 잔액 감소
        잔액 출금 금액이 0원 미만이라면 출금 불가
    5 계좌 정보를 출력하느 인스턴스 print_account_info() 구현
    6. 두개의 계좌를 생성 입금과 출금 수행 후 계좌정보 출력
'''
class BankAccount:
    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance

    def print_account_info(self):
        print(f"계좌 소유자 : {self.owner}\n계좌 번호 : {self.account_num}\n현재 잔액 : {self.balance}\n")

    def set_owner(self,owner):
        self.owner = owner

    def set_account_num(self, account_num):
        self.account_num = account_num

    def set_balance(self, balance):
        self.balance = balance

    def get_owner(self):
        return self.owner

    def get_account_num(self):
        return self.account_num

    def get_balance(self):
        return self.balance

    def deposit(self, money):
        if money <= 0:
            print(f"{money}원은 입금할 수 업는 금액입니다. \n")
            return
        self.balance += money
        print(f"{money}원 출금 되었습니다.\n현재 잔액 : {self.balance}원\n")

    def withdraw(self, money):
        if money <= 0:
            print(f"{money}원은 입금할 수 업는 금액입니다. \n")
            return
        if self.balance -money < 0:
            print("잔액이 부족하여 출금할 수 없습니다.")
            return
        self.balance -= money
        print(f"{money}원 출금 되었습니다.\n현재 잔액 : {self.balance}원\n")

account1 = BankAccount("홍길동","123-456-789",100000)
account2 = BankAccount("신사임당","987-654-321",500000)

account1.print_account_info()
account2.print_account_info()

account1.deposit(50000)
account1.withdraw(200000)

account2.deposit(50000)

account1.print_account_info()
account2.print_account_info()

account1.withdraw(60000)
account2.withdraw(60000)

account1.print_account_info()
account2.print_account_info()
