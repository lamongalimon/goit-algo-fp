import turtle


def tree(t, length, level):
    if level == 0:
        return
    t.forward(length)                        
    t.left(45)                              
    tree(t, length * 0.707, level - 1)       
    t.right(90)                              
    tree(t, length * 0.707, level - 1)       
    t.left(45)                               
    t.backward(length)  


def main():
    try:
       level = int(input("Please indicate the level of recursion: "))
    except ValueError:
       print("Level must be a whole number")
       return                        

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)                           
    turtle.tracer(0)
    
    tree(t, 100, level)
    turtle.update()
    turtle.done()


main()