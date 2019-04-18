"""# Lists

Note: You should already be familiar with the lessons in the `basic_logic` section that cover
looping and indexing.

Lists are the first workhorse container you'll want to know, inside and out. But what are lists used for?

Lists are used when we want to have an *arbitrary number* of data elements in a *particular order*.

Lists are all about mutability (adding and removing data elements from the container) and position
(answering questions like first, last, etc).

## Creating lists

Like most of the builtin types, lists have a constructor and a "literal" syntax.

When we made strings we just enclosed some characters in a string delimiter like "red" or
"blue". Alternatively we could call the string type to get a new empty string made for us:

>>> str()
''

The same is true of lists. There is a list type we can call to get a new empty list:

>>> list()
[]

This shows us that the literal syntax for lists involves an opening and closing square bracket. We
could also try passing data to the list constructor to see if it can be converted into a list:

>>> list(1)
Traceback (most recent call last):
  ...
TypeError: 'int' object is not iterable

This is interesting - the int type is a scalar type which only has a single indivisible value. You
can't make a list out of that! What about out of a string?

>>> list("red")
['r', 'e', 'd']

That works - and shows us the literal syntax for creating a list with data in it. You still use the
square brackets but add individual data items separated by a comma. Lists are heterogeneous so the
data does not all have to be of the same type.

>>> [1, 2, "a", "string"]
[1, 2, 'a', 'string']

## Manipulating lists

As with all other container types we use the builtin function `len` to get the number of elements in a container.

>>> name = list('python')
>>> name
['p', 'y', 't', 'h', 'o', 'n']
>>> len(name)
6

We use the `in` operator to test for containment. This works for strings and other containers too:

>>> 'p' in name
True

We can also use indexing to modify the data in the list because lists are mutable!

>>> name[0] = 'P'
>>> name
['P', 'y', 't', 'h', 'o', 'n']

However you can't assign to an index that doesn't currently have data.

>>> name[10] = 'test'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range

To append an item to the end of a list you need to use list methods. Take a look at them
(`help(list)` and skip the __magic__ methods). There aren't that many methods to know but notice
that many of them have a docstring like append: `L.append(object) -> None -- append object to end`

That `-> None` tells us that the function doesn't return anything but mutates the object it is
called against.

Sometimes we want to append all the items from a list to another list. Build a function that
mutates its input like append does:

>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> append_many(x, y)
>>> x
[1, 2, 3, 4, 5, 6]

Hopefully you used a for loop and called append repeatedly. But that's not the only way to do it!
See the help on `list.extend` for the built in version of this. You could also use the +
operator. On strings it concatenates two strings - on lists it concatenates two lists.

>>> [1, 2] + [3, 4]
[1, 2, 3, 4]

For removing values you can use the `list.pop` method. By default it removes and returns the last item in the list.

>>> a_list = list("red")
>>> a_list.pop()
'd'
>>> a_list
['r', 'e']

Go ahead and build a function that removes items from a list starting from the end until it finds a
target value. If it never finds the target value it empties the list.

>>> haystack = [1, 2, 3, 4]
>>> pop_till(haystack, 2)
>>> haystack
[1, 2]
>>> pop_till(haystack, 9)
>>> haystack
[]

I tend to dislike APIs like this that mutate their input arguments. An immutable version would be
easier to test and generally avoiding "side effects" is a good idea. Let's rewrite that last
function in immutable style. You might look at the list methods to see if there's an easy way to
make a copy of a list:

>>> newhaystack = [1, 2, 3, 4]
>>> pop_till_immutable(newhaystack, 2)  # just return values
[1, 2]
>>> newhaystack                         # and leave mutable arguments alone
[1, 2, 3, 4]

Note: You can generally make a copy of a container by passing it to its own constructor.

>>> newlst = list(newhaystack)
>>> newlst == newhaystack               # the values are equivalent
True
>>> newlst is newhaystack               # but they are two objects in differing memory locations
False

# Using lists as stacks and queues

Not only can you `.append`/`.pop` to affect the end of the list, you can also use `.insert(index,
val)` and `.pop(index)` to add to the list and remove from the list at an arbitrary
position. `.insert` will insert before your index so  use and index of 0 to insert at the very beginning.

Let's try a FIFO (First In, First Out) queue with a list. (You provide the functions!)

>>> q = []
>>> insert(q, 1)
>>> insert(q, 2)
>>> pop(q)
1

Can we make a LIFO (Last In, First Out) stack with a list? (You know what to do!)

>>> q = []
>>> push(q, 1)
>>> push(q, 2)
>>> q
[1, 2]
>>> pop(q)
2

NOTE: Think carefully about the O(N) runtime of these operations. Lists in python are not linked
lists but arrays of pointers. What do you think is the O(N) magnitude of removing an item from the
end of a list? How about the O(N) of adding a new item at the head of the list?

If you intend to use a list as a queue consider importing `collections.deque` instead.

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python3 using_lists.py

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
