#turtle 모듈 사용 Turtle, Screen 클래스 import
from turtle import Turtle, Screen
import random
t = Turtle()        # Turtle 클래스의 객체 생성, 이름 t
screen = Screen()   # Screen 클래스의 객체생성\
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
t.speed(0)
# 랜덤 객체를 생성
random = random.Random()
colors = [
    "dodger blue",
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]

def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

def draw_frigures(num):
    t.color(random.choice(colors))
    if num < 3:
        print("도형을 그릴 수 없습니다.")
        return
    for _ in range(num):
        t.forward(100)
        t.left(360/ num)


def draw_dotted_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360 / num)

'''
    .heading() 메서드:
        거북이가 바라보는 방향으로 나태는 속성을 도(degree) 단위로 나타남.
        
        해당 메서드는 콘솔창에서 float 형태로 나옴 
        0도 : 동
        90도 : 북
        180도 : 서 
        270도 : 남
    .setheading() 메서드 : 
        특정각도로 거북이를 회전시키는 메서드
    .circle()메서드 :
        거북이가 원 그리는 메서드
'''

def draw_spriograph(size_of_gap):
    if size_of_gap == int(size_of_gap):
        for _ in range(360 // size_of_gap):
            t.color(random.choice(colors))
            t.circle(100)
            t.setheading(t.heading() + size_of_gap)
            t.circle(100)
    else:
        print("도형을 그릴 수 없습니다.")
        return

draw_spriograph(7)

screen.exitonclick()