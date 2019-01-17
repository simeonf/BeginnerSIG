"""Let's learn about functions!

# About Functions!

Functions in Python let us give a name to a little chunk of code and then run it by saying its name
+ the "call operator". Don't worry every time you've typed `exit()` you're already doing this. The
"exit" part is the name of a function and the "()" part is the call operator.

"Calling" a function means running the code it contains and you have probably called some functions already.

As you may know you can put bits of data between those parentheses to "pass" arguments to a function. For example:

>>> min
<built-in function min>
>>> min(1, 3)
1

The function named min exists and if you see its name, the output is the thing the name is pointing
to. But to run it you need to use the parentheses and pass it arguments. Can you guess what min does?

# Defining Functions

You can also define your own functions. Functions are declared with a special keyword "def", a name
which can include letters, numbers, and the underscore and is followed by parentheses. Functions have an
indented body - the code that does the function's action. For example:

>>> def some_function():
...     return 1
>>> some_function()
1

Does that example make sense? It defined a function that produces a value (use the "return"
statement in the function to make the value the function produces). Then it calls the function to check that it works.

But what if you wanted to pass data to the function? In that case you would put some names (we call em "parameters") inside the function's parentheses.

Then in the body of the function you can reference that name to get the value that was passed in. Let's see it in action:

>>> def plus_1(x):
...     return x + 1
>>> plus_1(10)
11
>>> def some_function(x, y):
...     return x + y
>>> some_function(1, 2)
3


Does that make sense to you? Let's give you some examples of function calls that fail and have you
define the functions below to make the examples pass.

# Examples for you to implement

Make these examples pass by defining functions.

First make function that takes two arguments and returns the addition of the two values. You could
cheat a bit by reading carefully above!

>>> add_two(4, 5)
9

What about a function that adds up three values?

>>> add_three(1, 2, 3)
6

How about a function that when passed anything at all, just returns whatever it was passed?

>>> identity("test")
'test'
>>> identity(1)
1

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python getting_started.py

You should see a report of successes and failures.

To make the failing tests pass, add your own Python code or edit the partial completions in the
space below.

"""

# DO NOT EDIT ABOVE THIS LINE
# Add (or edit) python code below this comment block


# DO NOT EDIT BELOW THIS LINE
# Add (or edit) python code above this comment block

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if results.failed == 0:
        print("Success! All exercises passed!")
