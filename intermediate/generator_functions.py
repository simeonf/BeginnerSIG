"""# Generator Functions

Laziness is very important to Python, particularly in Python 3. You've already noticed that many
built in functions are lazy - they essentially return the instructions required to produce a data
structure instead of the data structure directly.

In Python 2 running range(10000000) might crash your computer - it makes a list with the numbers from 0 to a billionty. Yes that's a real number :)

But Python 3 returns a "range object" which can be iterated over and on demand produces the next value in the sequence. But lazily - it doesn't give you the next number till you need it... Can we make our own lazy objects?

There is an object oriented way to make generators but I love the sweet sweet syntactic sugar
provided by the `yield` keyword.

Check it out - putting yield in a function is like putting return in a function but it makes your
function not a function plus it pauses your function instead of terminating it.

Maybe I should just show you:

>>> def infinite_1():
...     while True:
...         return 1


Quick question - if I call this function how many 1s will I get back?

>>> infinite_1()
1

Only one 1! (Were you right?) Because return terminates the function even in an endless loop. But what if used yield?

>>> def infinite_1():
...     while True:
...         yield 1
>>> x = infinite_1()
>>> type(x)
<class 'generator'>

Huh. I called my function but didn't get any 1s back. Instead I get back a "generator object". What can you do with a generator? Well usually you might for-loop over them but this one is infinitely long. Let's just call next() on it.

>>> next(x)
1
>>> next(x)
1

Let's try this one more time with some instrumentation to see what's going on.

>>> def infinite_1():
...     while True:
...         print("Before yield")
...         yield 1
...         print("After yield")
>>> x = infinite_1()

Nothing happens! We called our function... but it didn't call our function yet, just wrapped it up
in a generator as before. Let's try next():

>>> next(x)
Before yield
1
>>> next(x)
After yield
Before yield
1

Pretty cool! We have a (paused) function in an infinite loop. Let's use this laziness to implement our own version of range. (Hint: use a while loop!)

>>> type(myrange(4))
<class 'generator'>
>>> for x in myrange(3):
...     print(x)
0
1
2
>>> for x in myrange(0,4,2):
...     print(x)
0
2


Like this? Why not also implement a generator that implements a useful infinite sequence?

>>> colors = cycle(['blue', 'gray'])
>>> next(colors)
'blue'
>>> next(colors)
'gray'
>>> next(colors)
'blue'

You might look at all the cool stuff in the built in itertools module - cycle lives there and many other functional goodies.

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python generator_functions.py

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
