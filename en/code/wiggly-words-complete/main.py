from turtle import *
from random import randint

penup()
hideturtle()
speed(20)

phrase1 = list('Wiggly words')  # List from a string
style1 = ('Courier', 20)

phrase2 = list('growing up')
style2 = ('Times New Roman', 14)

phrase3 = list('falling down')
style3 = ('Arial', 24)

phrase4 = list('round and round ')
style4 = ('Georgia', 18)

phrase5 = list('and round and round they go')
style5 = ('Georgia', 12)

# first line
goto(-140, 140)
right(90)
color('hotpink')
for i in range(len(phrase1)):  #  Gets length of a list
    write(phrase1[i], font=style1, align='center')
    forward(15)
    right(randint(-8,8))

# up line
forward(30)
left(90)
forward(30)
left(90)
color('dodgerblue')
for i in range(len(phrase2)):
    write(phrase2[i], font=style2, align='center')
    forward(15)

# falling down
right(120)
forward(30)
color('limegreen')
for i in range(len(phrase3)):
    write(phrase3[i], font=style3, align='center')
    forward(randint(15,20))
    right(randint(2,3))

# circle here
goto(80, 100)
color('orange')
for i in range(len(phrase4)):
    write(phrase4[i], font=style4, align='center')
    forward(20)
    right(360 / len(phrase4)) #  turn fraction of a circle

# spiral
goto(120, -50)
color('blueviolet')
step = 10  # starting step size - gets bigger each time
for i in range(len(phrase5)):
    write(phrase5[i], font=style5, align='center')
    right(40)
    forward(step)
    step += 1  # increase this to spiral out faster
