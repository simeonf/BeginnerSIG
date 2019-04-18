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

Important! The name "args" is arbitrary. You could call it something
else - but its a tradition to call this parameter args.

Can you make add take an arbitrary number of arguments?

>>> add(1, 2, 3)
6
>>> add(1, 2, 3, 4)
10

# What about names?

It's also important to note that `*args` only helps you with
positional arguments. You may not realize it but you can also pass
arguments by name! For instance make a subtract function with
parameter names x and y. It should work like this:

>>> subtract(5, 2)
3

That's pretty normal - the `5` above is the first positional argument
and it went to the first parameter in your function definition, the
`2` is the second positional argument and went to the second
parameter. But what if I called it like this?

>>> subtract(y=2, x=5)
3

Huh! You can pass arguments by name in which case position doesn't
matter! So how about our old friend variadic? Can we pass it arguments by name?

>>> variadic(x=1)
Traceback (most recent call last):
...
TypeError: variadic() got an unexpected keyword argument 'x'

It turns out *args only helps us with positional arguments. To catch
arguments that are passed by name you need *args starry friend
**kwargs! Just like *args is a catchall for unaccounted for positional
args, **kwargs is a catchall for unaccounted for named arguments.

>>> def variadic2(**kwargs):
...     return kwargs
>>> variadic2(x=1, y=2) == {'x': 1, 'y': 2}
True

So consider how to write functions that can be called like this:

>>> color(255)
(255, 0, 0)
>>> color(red=255)
(255, 0, 0)
>>> color(255, 10, 1, alpha=1.4) # you don't have to do anything with alpha
(255, 10, 1)
>>> color(255, 10, 1, extra="foo") # or extra. Just don't crash!
(255, 10, 1)

Why would you ever want to use **kwargs? Hint: checkout the help for `dict`.

# Calling with * and **

Calling a function with * and ** is just like defining, but the inverse.

In a def line * and ** pack incoming values (or name/value pairs) into
a container. When calling a function * unpacks a positional container
into positional args and ** unpacks a dict into named args.

Assuming you named your function with red, green and blue arguments you might have data in a list:

>>> color_list = [255, 200, 100]
>>> color(*color_list)
(255, 200, 100)
>>> color_dict = {'red': 255, 'green': 200, 'blue': 100}
>>> color(**color_dict)
(255, 200, 100)

Does this make sense?

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
