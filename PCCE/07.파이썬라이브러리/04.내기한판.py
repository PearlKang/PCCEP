from re import T
import turtle


import turtle as t
import random
import time

# 가로 800, 세로 800 배경변경
t.setup(width=800, height=800)
t.shape("turtle")
t.color("orange")
t.bgcolor("steelblue")

# 중앙선 만들기
t.goto(0,400)
t.goto(0,-400)
t.goto(0,0)

# 속도 변경
t.speed(1)

# 펜 올리기
t.penup()

# 10회 이동
for i in range(10):
    t.forward(random.randint(-50,50))
    time.sleep(1)

# x죄표 체크
if t.xcor() > 0:
    t.write("turtle goes right",font=("Arial",16))
elif t.xcor() < 0:
    t.write("turtle goes left",font=("Arial",16))
else:
    t.write("turtle goes center",font=("Arial",16))

# 화면 클릭 되었을 때 종료
t.exitonclick()