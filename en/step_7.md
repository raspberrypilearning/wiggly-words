## Make words go around in a circle

Add `phrase4` text and choose `style4` font.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15
line_highlights: 17-18
---
style3 = ('Arial', 24)

phrase4 = list('round and round ')
style4 = ('Georgia', 18)
--- /code ---

</div>

Use another loop and a turn angle to place words around a circle.

> ### Tip
>
> `360 / len(phrase4)` splits a full turn into equal parts.
{: .c-project-callout .c-project-callout--tip}

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 47
line_highlights: 51-57
---
    write(phrase3[i], font=style3, align='center')
    forward(randint(15,20))
    right(randint(2,3))

# circle
goto(80, 100)
color('orange')
for i in range(len(phrase4)):
    write(phrase4[i], font=style4, align='center')
    forward(20)
    right(360 / len(phrase4)) #  turn fraction of a circle
--- /code ---

</div>


### Now run your code

The words appear arranged in a circle on the right of the screen. Change the number in `forward(20)` to change the circle size.

<div class="c-project-output">

![Three animated lines of poetry appear in different colours and directions, with an orange phrase arranged in a circle on the right side of the screen.](images/step7.png)

</div>
