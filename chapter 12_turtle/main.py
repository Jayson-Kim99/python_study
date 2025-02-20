#turtle 모듈 사용 Turtle, Screen 클래스 import
from turtle import Turtle, Screen

t = Turtle()        # Turtle 클래스의 객체 생성, 이름 t
screen = Screen()   # Screen 클래스의 객체생성\
t.shape("turtle")
t.color("white")
screen.bgcolor("black")

# for _ in range(10): # 반복 10번 하는 것 변수 사용 X 라서 _ 사용
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# t.left(90)
# t.forward(100)

for _ in range(3):
    t.forward(100)
    t.left(120)
for _ in range(10):
    t.back(100)
    t.left(80)

for _ in range(10):
    t.back(100)
    t.right(80)





screen.exitonclick()