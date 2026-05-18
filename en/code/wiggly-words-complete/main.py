from turtle import *
from random import randint

penup()
hideturtle()

line1 = list('Wiggly words')  # List from a string
style1 = ('Courier', 20)

line2 = list('growing up')  
style2 = ('Times New Roman', 14)

line3 = list('falling down')  
style3 = ('Arial', 24)

line4 = list('round and round ') 
style4 = ('Georgia', 18)

line5 = list('and round and round they go')
style5 = ('Georgia', 12)

# first line
goto(-150, 100)
right(90)
color('hotpink')
for i in range(len(line1)):  #  Gets length of a list
    write(line1[i], font=style1, align='center')
    forward(15)
    right(randint(-8,8))

# up line
forward(30)
left(90)
forward(30)
left(90)
color('dodgerblue')
for i in range(len(line2)): 
    write(line2[i], font=style2, align='center')
    forward(15)
 
# falling down
right(120)
forward(30)
color('limegreen')
for i in range(len(line3)): 
    write(line3[i], font=style3, align='center')
    forward(randint(15,20))
    right(randint(2,3))

# circle here
goto(80, 100)
color('orange')
for i in range(len(line4)):
    write(line4[i], font=style4, align='center')
    forward(20)
    right(360 / len(line4)) #  turn fraction of a circle

# spiral
goto(120, -50)
color('blueviolet')
step = 10  # starting step size - gets bigger each time
for i in range(len(line5)):
    write(line5[i], font=style5, align='center')
    right(40)
    forward(step)
    step += 1  # increase this to spiral out faster
