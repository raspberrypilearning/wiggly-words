## Make the letters wiggly

Play with random angles using `randint()` to add a random wobble to each letter.

> ### Tip
>
> `left(randint(-8,8))` chooses a random angle to turn the turtle left, between -8 and 8 degrees. 
{: .c-project-callout .c-project-callout--tip}

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 15
---
# first line
goto(-140, 140)
right(90)
for i in range(len(phrase1)): 
    write(phrase1[i], align='center')
    forward(15)
    right(randint(-8,8))
--- /code ---

</div>


### Now run your code
The letters appear with a random wobble each time you run it. 

<div class="c-project-output">

![Wiggly words displayed vertically, with each letter tilted at a slightly different angle to create a random wobble effect](images/step4.png)

</div>

> ### Tip
>
> `Experiment with different random values.
{: .c-project-callout .c-project-callout--tip}

