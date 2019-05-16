"""# Indexing

We'll want to become very proficient with the workhorse container data types (tuples, lists, dicts)
but for the moment we'll just deal with strings.

That's right - a string could be thought of as a sequence of individual characters. Strings have
length and individual characters can be indexed.

>>> len("Python")
6
>>> "Python"[0]
'P'

Python doesn't have a character type so what you get back when you index the string is a new string of length 1.

Indexing is just a way to specify which record in a container you want. Ordered containers can be
indexed with numbers and the first item in the container is item number 0. The last item has an
index of len - 1 but Python lets us cheat a little here:

>>> s = "Python rocks"
>>> len(s)
12
>>> s[len(s) - 1]
's'
>>> s[-1]
's'

You could think about negative indexes as counting back from the end
of the container so -1 is the last item, -2 is the second to last item,
and so on.

Sometimes you might define utility functions that hard code the index to return and just take a
container. Go ahead and build a "first" and "last" function. They should work like:

>>> first("Testing")
'T'
>>> last("Testing")
'g'

In python accesing an index that doesn't exist causes an error!

>>> "test"[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

Maybe we want our first and last functions to work even if passed an empty string. Use and if
statement to check the container and handle this special case so that the functions return `None`

>>> first("")  # returning None results in no output in the interactive interpreter
>>> last("")   # ditto

# Slices

Python also supports indexes that are a little more complicated. I think the easiest way to
understand slice arguments is to check out the builtin `range` function. Let's build a list with the `range` function!

>>> list(range(9))
[0, 1, 2, 3, 4, 5, 6, 7, 8]

Check out the help(range) to see the arguments - when passed a single number this is the "stop"
condition and we get all the numbers up to but not including stop.

Look at the output when we use more arguments:

>>> list(range(3,9))
[3, 4, 5, 6, 7, 8]

Yup - the first argument is the "start" and we get a list of numbers between start and stop
including start but not including stop. There's one more argument possible - check out this call:

>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]

We call that last argument the "step" and we could read that call to range as meaning: start at 0,
go to 10, jump by 2 instead of by 1.

Practice with the range function. It is useful and sometimes you do want lists of numbers like even
numbers or multiples of 25 up to 250. Don't ever type those out - programmers should be lazy and
prefer to let the computer do the data generation when possible!

We can now use that start, stop, step idea in the context of indexes! Put up to all three arguments separated by colons in the indexing operator and we get just what you might expect.

>>> s = "Slices aren't so bad!"
>>> s[0:4]
'Slic'
>>> s[0:]  # If you omit the stop it defaults to len of s
"Slices aren't so bad!"
>>> s[::2]  # If you omit the start it defaults to 0
'Sie rnts a!'

Play with slices in your shell and then write some functions that use slices:

>>> even_indexes(s)  # index 0, 2, 4, ....
'Sie rnts a!'
>>> odd_indexes(s)   # index 1, 3, 5, ...
"lcsae' obd"

Ready for a challenge? Can you figure out how to use slices to get the contents of the string reversed?

>>> reversed_string(s)
"!dab os t'nera secilS"

Slices aren't so bad!

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python indexing.py

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
