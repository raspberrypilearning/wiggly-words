## Make more lines of poetry

Add two more lists after `phrase1`. Replace the text with your own words.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11-15
---
phrase1 = list('My wiggly words')  # List from a string
style1 = ('Courier', 20)

phrase2 = list('growing up')
style2 = ('Times New Roman', 14)

phrase3 = list('falling down')
style3 = ('Arial', 24)
--- /code ---

</div>

Add the loops for the text.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 29
line_highlights: 32-49
---
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
--- /code ---

</div>

### Now run your code
Two more lines of the poem should animate. Experiment with the styles and position to draw the words how you want them.

<div class="c-project-output">

![Three lines of poetry are drawn in different directions, styles, and colours, with letters appearing one at a time](images/step6.png)

</div>
