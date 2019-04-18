"""# Dicts

Note: You should already be familiar with the lessons in the `basic_logic` section that cover
looping and indexing.

Dicts are another Python container you'll want to know, inside and out. But what are dicts for?

Dicts give you key -> value associations. Keys are unique but not really ordered. Dicts are also
mutable so you can add and remove key -> value pairs.

You could think about dicts as mapping names to values or as a pre-cached search tool. More on this later!

## Creating dicts

Like most of the builtin types, dicts have a constructor and a "literal" syntax.

>>> dict()
{}

This shows us that the literal syntax for empty dicts involves an opening and closing curly brace. We
could also try passing data to the list constructor to see if it can be converted into a list:

>>> dict(1)
Traceback (most recent call last):
  ...
TypeError: 'int' object is not iterable

We remember this from looking at the list type. But you could make lists from strings. How about dicts?

>>> dict("red")
Traceback (most recent call last):
  ...
ValueError: dictionary update sequence element #0 has length 1; 2 is required

Hmm. That doesn't work! Dictionaries can be made from sequences but they have to have the right shape!

We'll come back to that - let's try some other way of making dictionaries. We can use keyword
arguments to instanciate dictionaries like this:

>>> color = dict(red=0, green=155, blue=200)
>>> color
{'red': 0, 'green': 155, 'blue': 200}

That works - and shows us the literal syntax for creating a dict with data in it. This should be
familar if you've ever used json data - key value pairs separated by colons with commas between
each pair.

## Manipulating dicts

Of course the length of the dict is the number of keys it contains:

>>> len({'key1': 1})
1

We use the `in` operator to test for containment. This looks for keys, not for values. Dicts don't
know anything about their values, but they know about their keys!

>>> 'key' in {'key': 1}
True
>>> 1 in {'key': 1}
False

We can also use indexing to modify the data in the dict (because mutability)!

>>> color['red'] = 90
>>> color
{'red': 90, 'green': 155, 'blue': 200}

However unlike lists if you attempt to assign to a key that doesn't exist you don't get an error,
you create the key!

>>> color['alpha'] = .5
>>> color
{'red': 90, 'green': 155, 'blue': 200, 'alpha': 0.5}

The dict method `.pop()` takes a key and returns the corresponding value and removes the key from the dict.

>>> color.pop('alpha')
0.5
>>> color
{'red': 90, 'green': 155, 'blue': 200}

Now that 'alpha' isn't set you can't access it:

>>> color['alpha']
Traceback (most recent call last):
  ...
KeyError: 'alpha'

NOTE: You shouldn't think about dicts as ordered containers - there aren't functions for getting the
first or last value. However as of Python 3.7 dictionaries have a stable order.

Dicts do have some useful methods for handling failure gracefully or for "concating" two dicts. Use
`dir` and `help` and check em out!

## Using a dict to do something useful

You could use dictionary key uniqueness to count recurring values. For instance - write a function
that counts the words in a sentence:

>>> repeated_words("Python is a great language")
{}

>>> repeated_words("Python Python is a great language great")
{"Python": 2, 'great': 2}

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python3 using_dicts.py

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
