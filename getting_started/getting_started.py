"""This is a test driven exercise.

Exercises contain text meant just for humans - these are the explanations and intructions and this
sentence is an example of such text.

The exercises also contain parts that look like Python code entered in the interactive console. For instance the next two lines:

>>> "red,green,blue".split(',')
['red', 'green', 'blue']

The three arrows (">>> ") at the start of the first line indicate that what follows on this line is
Python code. The following line doesn't have these special characters so it is the output you would
see in the Python console.

These two lines define a test - some code that should run and the output you would see. You could
even copy and paste the first line (minus the ">>>") into a Python console and see the same output.

Code that works already may not teach you too much so you'll see code that doesn't work.

>>> my_first_exercise()
'Hello world'

There is no built in function called "testing" so we would expect this snippet to fail if we pasted it in a Python console.

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python getting_started.py

You should see a report of successes and failures.

To make the failing tests pass, add your own Python code or edit the partial completions in the
space below.

"""

# DO NOT EDIT ABOVE THIS LINE
# Add (or edit) python code below this comment block

def my_first_exercise():
    return "I don't think this is right"


# DO NOT EDIT BELOW THIS LINE
# Add (or edit) python code above this comment block

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if results.failed == 0:
        print("Success! All exercises passed!")
