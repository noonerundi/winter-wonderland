import turtle




screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')



t = turtle.Turtle()
t.speed(0)
t.pencolor('black')


#t.hideturtle()


t_ground=turtle.Turtle()
t_ground.speed(0)
t_ground.pencolor('white')
t_ground.fillcolor('white')




t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()







#stump
t.penup()
t.goto(200,0)
t.pensize(15)
t.pencolor('SaddleBrown')
t.pendown()
t.goto(200,-100)




#top tree
t.penup()
t.pencolor('green')
t.fillcolor('green')
t.goto(200,50)
t.pendown()
t.begin_fill()
t.goto(160,10)
t.goto(240,10)
t.goto(200,50)
t.end_fill()
t.penup()




#second part


t.goto(200,25)




t.pendown()
t.begin_fill()
t.goto(140,-25)
t.goto(260,-25)
t.goto(200,25)
t.end_fill()
t.penup()




#third part
t.goto(200,0)
t.pendown()
t.begin_fill()
t.goto(120,-50)
t.goto(280,-50)
t.goto(200,0)
t.end_fill()




t.pensize(1)
t.pencolor('black')





t.penup()
t.goto(0,-100)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(35)
t.end_fill()


t.penup()
t.goto(0,-60)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(0,-20)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(25)
t.end_fill()



t.penup()
t.goto(0,-30)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(0,-40)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(0,-50)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()



t.penup()
t.goto(10,10)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-10,10)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()



t.pensize(7)
t.pencolor('sienna4')
t.penup()
t.goto(-25,-30)
t.pendown()
t.goto(-60,-20)


t.penup()
t.goto(25,-30)
t.pendown()
t.goto(60,-20)



t.penup()
t.goto(0,-10)
t.pendown()

t.penup()
t.goto(0,250)
t.pendown()
t.write("Merry Christmas", font=("arial", 30, "bold"), align="center")
t.pencolor("brown")
t.fillcolor()



turtle.done()

