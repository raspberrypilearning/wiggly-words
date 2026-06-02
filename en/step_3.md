## Make a loop for the first line

Replace the code that writes `phrase1[0]` with this loop.

> ### Tip
>
> The loop writes each letter in `phrase1` one at a time.
{: .c-project-callout .c-project-callout--tip}


<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 11-14
---
# first line
goto(-140, 140)
right(90)
for i in range(len(phrase1)): 
    write(phrase1[i], align='center')
    forward(15)
--- /code ---

</div>

### Now run your code
The letters in `Wiggly words` appear one at a time.


<div class="c-project-output">

![The letters in "Wiggly words" appear one under another](images/step3.png)

</div>

> ### Tip
>
> `len(phrase1)` counts how many letters are in the list.
{: .c-project-callout .c-project-callout--tip}

> ### Debugging
>
> The two lines inside the loop must be indented.
{: .c-project-callout .c-project-callout--debug}
