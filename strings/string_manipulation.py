'''
# Strings

Strings in Python are the data type used to store what we think of as text. My name "Simeon Franklin" is a string.

Like most of the built in types there are two ways to make strings in Python. There is a constructor that makes a new string for you:

>>> str()
''

That '' is an empty string - a string with no contents. We often think of string contents as a
length - how many characters are there? There is a built in function for that:

>>> len('')
0
>>> len('Simeon')
6

As you can see there is also a "literal" syntax for making strings. You can just type them in while
surrounding them with quotes. Single quotes work, double quotes work, triple quotes work!

>>> "a"
'a'
>>>

"""a"""'a'

The quotes aren't part of the string - that string "a" has a length of 1 no matter what kind of quotes you used to make it.

# String operations

There are some operators that apply to strings. You should check out both * and +. Can you write a function that uses one or the other to double a string?

>>> double_string("foo")
'foofoo'

Python also has an `in` operator that is used for searching.

>>> "y" in "Python"
True

# String Methods

Strings are often used a little differently than numbers in that we often call methods on strings.

For now lets just think of methods as functions that happen to live on string objects. It's less
complicated than it sounds - just use the `.` operator.

>>> name = "Simeon"
>>> name.upper()
'SIMEON'

There are a lot of string methods! Check out what happens when you try running `help(str)`!

# Time to make you do some work!

Be sure to look at the help or read https://docs.python.org/3/library/stdtypes.html#string-methods

You should already know about boolean operators and `if` statements.

Then implement the following functions to make the tests pass.

Maybe we want to be able to say things about the contents of strings. Can string methods help us?

>>> either_numbers_or_letters("Simeon")
True
>>> either_numbers_or_letters("123")
True
>>> either_numbers_or_letters("Simeon123")  # This one has both letters and numbers
False

Sometimes we want to format strings for fixed width output. Can string methods help us?

>>> cell("1,000")
'     1,000'
>>> len(cell("1,000"))
10

Sometimes we want to remove errant characters from strings. Can string methods help us?

>>> numeric_cell("1,000")  # Don't get to hung up on doing this right - figure out how to remove that pesky comma!
'      1000'

There are many many string methods - check em all out!


# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python string_manipulation.py

You should see a report of successes and failures.

To make the failing tests pass, add your own Python code or edit the partial completions in the
space below.

'''

# DO NOT EDIT ABOVE THIS LINE
# Add (or edit) python code below this comment block


# DO NOT EDIT BELOW THIS LINE
# Add (or edit) python code above this comment block

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if results.failed == 0:
        print("Success! All exercises passed!")
