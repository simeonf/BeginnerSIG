"""# Operators

Operators in Python are the pieces of punctuation - the +, -, and so on. But even the trusty dot
"." or the paired parens or various kinds of braces are considered operators.

Types often get mentioned in conjunction with operators because that "+" symbol might do different
things depending on what *kind* of data is on both sides.

For instance:

>>> 1 + 1
2
>>> 1 + "test"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

You might want to peek at the official docs which define the basic types and the operators that
work on them. But for the moment let's not worry so much about types.

Let's go ahead and define some calculator functions. The following examples won't work - until you
do your magic!

>>> add(1, 3)
4
>>> subtract(3, 1)
2
>>> multiply(2, 4)
8
>>> divide(9, 2)
4.5

You probably know all the operators you need for these functions. But what does "**" do? (Hint: try
opening a python console and trying out `4 ** 2`) And how about the "%"?

>>> power(2, 3)
8
>>> remainder(9, 2)
1

# Let's use the if-statement

In Python you can use the if to choose whether to execute a branch of code. For instance:

>>> if 4 > 5:
...     print("Is math broken?")

Note that there's no output - that print statement never executed because the if statement makes it
"conditional". The indented body of the if statment only executes if the logical statement in the
if is true.

You can also make an if statement with two branches:

>>> if 4 > 5 :
...     print("Is math broken?")
... else:
...     print("Math isn't broken!")
Math isn't broken!

Go ahead and make a function called bigger that returns whichever of the two input arguments is, uh, bigger!

>>> bigger(4, 5)
5
>>> bigger(20, 1)
20

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python operators_and_if.py

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
