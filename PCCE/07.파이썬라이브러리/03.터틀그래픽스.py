# import turtle

# # 거북이 모양으로 변경
# turtle.shape("turtle")

# # 화면을 클릭할 때 종료
# turtle.exitonclick()

# =>
import turtle as t

# 거북이 모양으로 변경
t.shape("turtle")

# 색변경
t.color("orange")
t.bgcolor("steelblue")

# 속도 조절 1 ~ 10
t.speed(1)

# 앞으로 가기
t.forward(200)

# 방향 전환 (왼쪽으로 90도)
t.left(90)
t.forward(200)

# 특정 좌표로 이동
t.goto(0,200)

# 펜 올리기
t.penup()
t.forward(-200)

# 화면을 클릭할 때 종료
t.exitonclick()