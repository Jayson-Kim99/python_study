'''
외부 패키지의 설치
좌측 상단 메뉴버튼(햄버거) > file > settings(설정 : ctrl + alt + s)
좌측 리스트에서 project : 프로젝트명으로 되어있는 부분
> python interpreter
> 좌상단 + 눌러서 필요한 패키지 검색 및 설치
'''
from tkinter.scrolledtext import example

from prettytable import PrettyTable
from pokemon_data import pokemon_data

table = PrettyTable()
pokemons_data = pokemon_data

table.field_names = ["번호", "이름", "타입"]
for i in range(0,26,1):
    table.add_row(pokemons_data[i])
print(table)