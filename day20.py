from turtle import Screen
import time
from snake import Snake 
from food import Food
from score_borad import Score_Board

# Screen setup
screen = Screen()
screen.tracer(0)  
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.listen()

#components
snake = Snake()
food = Food()
score_board = Score_Board()



#control 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#moving 
game_is_on = True
sleep_time = 0




while game_is_on:
    screen.update()  
    time.sleep(0.1)
    snake.move() 

    #food and snake connection
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extand()

    #wall game_over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_is_on = False

    #snake_itself_game_over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()            
        


    
    
    
    
    
    
   

screen.exitonclick()