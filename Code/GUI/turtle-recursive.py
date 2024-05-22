import turtle

def draw_branch(branch_length):
    if branch_length > 5:
        # 현재 가지 그리기
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 오른쪽 가지
        turtle.left(40)
        draw_branch(branch_length - 15)

        # 왼쪽 가지
        turtle.right(20)
        turtle.backward(branch_length) # 원래 위치로 돌아가기

def draw_tree():
    turtle.left(90) # 나무를 세우기 위해 왼쪽으로 90도 회전
    turtle.penup()
    turtle.backward(100) # 화면 하단으로 이동
    turtle.pendown()
    turtle.color("brown")
    draw_branch(100) # 나무 가지 그리기 시작
    turtle.exitonclick() # Turtle 창 자동 종료 방지

turtle.speed("fastest") # 그리는 속도 설정
draw_tree()
