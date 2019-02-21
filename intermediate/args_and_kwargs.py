"""# Let's learn about *args and **kwargs

First we should get some terminology out of the way:

- arguments are the values passed to a function when we call it
- parameters are the names declared by the function in its definition

Arguments and parameters in Python come in two flavors:

- positional, required
- named, default value, optional

# Let's check out the reason for these two kinds of things

Make a function called `add`. Add should take two numbers and return the result:

>>> add(5, 2)
7

But what if we left the second argument off? If your def line looks
like `def add(x, y):` then your code will crash. But we can give
default values to our parameters by adding and equal sign in the def
line like `add(x, y=1):`.

This has the cool effect of making the y parameter optional. Go ahead
and modify your function so that

>>> add(10)
10

works.

# Variadic functions

That's cool - a parameter can have a default value and use it if the call didn't provide a value.

But what about a function like `zip` (or `max` or `min`). How many arguments do they take?

Variadic functions could be called with as many arguments as you
like. In Python you can define a function with a placeholder parameter
which will hold any *positional* arguments passed to the function. It works like this:

>>> def variadic(*args):
...     return args
>>> variadic(1, 2, 4)
(1, 2, 4)

As you can see args is a tuple of all the values passed into the function.

Can you make add take an arbitrary number of arguments?

>>> add(1, 2, 3)
6
>>> add(1, 2, 3, 4)
10

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python args_and_kwargs.py

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
