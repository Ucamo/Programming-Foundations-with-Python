import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    
    

    #draw_circle()
    #draw_triangle()
    window.exitonclick()

def draw_square(turtle):
    cont=0
    while cont<4:
        turtle.forward(100)
        turtle.right(90)
        cont+=1
    

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    bob = turtle.Turtle()
    bob.shape("triangle")
    bob.color("green")

    cont =0
    while cont<3:
        bob.forward(300)
        bob.left(120)
        cont+=1
    
    
draw_art()
