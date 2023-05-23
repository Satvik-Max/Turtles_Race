from turtle import *
import random
screen = Screen()
screen.setup(width = 500 , height= 400)
is_bet = False
user_bet = screen.textinput(title=" CHOOSE YOUR BET ", prompt=" ENTER YOUR BET TURTLE ")
print(user_bet)
list_turtles = []
list = [-70 , -40 , -10 , 20 ,50 , 80]
colors = ["aqua","red","yellow","purple","green","blue"]

def playgame():
    list_turtles.clear()
    for i in range(0,6):   
        red = Turtle(shape="turtle")
        red.color(colors[i])
        red.penup()
        red.goto(x=-230,y=list[i])
        list_turtles.append(red)
    if user_bet:
        is_bet=True
    while is_bet:
        for t in list_turtles:
            if t.xcor() > 230 :
                winning_color= t.pencolor()
                if winning_color == user_bet:
                    print(f" YOUU WIN AND YOUR COLOR IS {user_bet}")
                else:
                    print(f" YOUU lOST AND YOUR COLOR IS {user_bet} WINNING COLOR {winning_color} ")
                is_bet = False
            random_speed = random.randint(0,10)
            t.forward(random_speed)
playgame()
for i in list_turtles:
        i.clear()
        i.home()
if textinput(title=" your opinion ", prompt="WANNA PLAY AGAIN ").lower()=='yes':
    screen.clear()
    playgame()
else:
    exit()
screen.exitonclick()