"""
Python Guessing Game
Ask the user to guess the year when Python 1.0 was released (the correct answer is 1994) with the following prompt:

When was Python 1.0 released? << remember to add a space at the end of this prompt

If the user answers 1994, show:

Correct!

and finish the program. If the user answers with any year that is later than 1994, show a hint and ask again for a new year on a new line:

It was earlier than that!
When was Python 1.0 released? << remember to add a space

If the user answers with any year that is earlier than 1994, show a hint and ask again for a new year on a new line:

It was later than that!
When was Python 1.0 released? << remember to add a space
"""

# Create an indefinite loop (while True) to repeatedly ask the user for input.
while True:
    # Prompt the user for the release year of Python 1.0 and convert the input to an integer.
    python_year = int(input('When was Python 1.0 released? '))
    
    # Check if the input year is less than 1994.
    if python_year < 1994:
        print('It was later than that!')
    # Check if the input year is greater than 1994.
    elif python_year > 1994:
        print('It was earlier than that!')
    else:
        # If the input year is equal to 1994, print 'Correct!' and exit the loop.
        print('Correct!')
        break
