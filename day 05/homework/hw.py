import turtle

# ფუნქცია სასახლე
def draw_palace():
    # ეკრანის შექმნა
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    
    palace = turtle.Turtle()
    palace.shape("turtle")
    palace.speed(5)
    
    # დახაზოს სასახლის ძირითადი ნაწილი (ოთახი)
    palace.penup()
    palace.goto(-100, -100)
    palace.pendown()
    palace.begin_fill()
    palace.color("gold")
    for _ in range(4):
        palace.forward(200)
        palace.left(90)
    palace.end_fill()
    
    # დახაზოს სასახლის გუმბათი
    palace.penup()
    palace.goto(-150, 100)
    palace.pendown()
    palace.begin_fill()
    palace.color("purple")
    palace.setheading(45)
    for _ in range(4):
        palace.forward(212)
        palace.left(90)
    palace.end_fill()

    # დახაზოს სასახლის კოშკი
    palace.penup()
    palace.goto(-50, 100)
    palace.pendown()
    palace.setheading(0)
    palace.begin_fill()
    palace.color("brown")
    for _ in range(4):
        palace.forward(50)
        palace.left(90)
    palace.end_fill()
    
    # ჭერი (გუმბათი)
    palace.penup()
    palace.goto(-25, 150)
    palace.pendown()
    palace.setheading(45)
    palace.begin_fill()
    palace.color("red")
    palace.circle(40, steps=4)
    palace.end_fill()

    # სასახლის ფანჯარა
    palace.penup()
    palace.goto(-60, 50)
    palace.pendown()
    palace.setheading(0)
    palace.begin_fill()
    palace.color("lightblue")
    for _ in range(4):
        palace.forward(30)
        palace.left(90)
    palace.end_fill()

    # გრაფიკის დასრულება
    palace.hideturtle()
    screen.mainloop()

# გავუშვათ კოდი
draw_palace()