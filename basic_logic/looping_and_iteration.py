"""# Looping and Iteration

Loops in Python are ways to run a block of code repeatedly. Frequently
this happens because we want to manipulate "containers" - data types
that may contain multiple values.

We'll want to become very proficient with the workhorse container data types (tuples, lists, dicts)
but for the moment we'll just deal with strings.

That's right - as you learned in the indexing lesson a string is a sequence or container for individual characters.

Not only can you index into strings, you can loop over them. Let's practice a couple kinds of loops.

## `while` loops

Like most languages Python has a while loop. This is a chunk of code with a logical condition like
an if statement - but instead of running once if the condition is true it runs over and over again
as long as the condition continues to evaluate as true. So to loop through a string we might do
something like:

>>> s = "Python rocks"
>>> x = 0
>>> while x < 4:
...     print(s[x])
...     x = x + 1
P
y
t
h

The while loop does let us write loops where we don't know in advance how many times we'll be
iterating. For instance you might use a while loop to process some data when you'll stop based on
the data. For instance - you could write a function that processes some data and stops when it sees
a target value and returns the first index of the target

>>> find_needle('Python rocks', ' ')
6

If you don't find the value, return None.

>>> find_needle('Python rocks', 'x')
None

Go ahead and implement this with a while loop - but also check out help(str.index) when you're done!

## `for` loops

However! Most loops in Python are `for` loops. For loops are when you just want to iterate over a
container and don't actually care about the indexes. For loops look this:


>>> for num in range(3):
...     print(num)
0
1
2

The for-loop syntax has four parts: the "for" keyword, a variable name (we chose "num") which will
receive items from the container, the "in" keyword last an iterable that for will loop over.

You will always type "for" and "in" but the rest is up to you. Many languages have a for loop that
is just shorthand for creating indexes like `for(x=0;x<MAX;x++)`

Notice our for loop gets us the items in the container instead of creating the index value to
extract the value from the container.

Use a for loop to write a function that counts occurences of a target character in a string:

>>> count_needle("python rocks", "o")
2

Go ahead and implement this with a for loop - but also check out help(str.count) when you're done!

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python looping_and_iteration.py

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
