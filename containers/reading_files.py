"""# Reading data from files

Frequently we'll need to use files and file-like objects to load
external data. At the very least you should know how to read data from
text files in a couple of ways.

Files certainly could be thought of as containers and like lists,
dicts, and strings, files have some useful methods you should be aware
of.

## Opening a file

The first thing we have to do is contruct a file object. Unlike dicts and lists where there is a
single type which representst the container there are actually several different kinds of files for
reading text or binary data in buffered or unbuffered fashion.

Because of this we don't typically call the file type's constructor - instead we call the `open`
function which is a factory for constructing and returning the correct kind of file.

>>>  f = open("../README.md")
>>>  type(f)
_io.TextIOWrapper

That `open` call takes a bunch of different parameters so you can open files in binary mode for
non-textual content or specify an encoding for the text. We'll keep things simple right now but
sometime be sure to read the docs at `help(open)`.

## Reading from a file

Now that we have a file object we can read from it. Be sure to check out the methods of the file
object which include

* .read() - character oriented reading (or byte oriented reading for binary files). Use if you want
  to read a fixed number of characters. Spoiler alert: you'll never want to do this!

* .readline() - returns a whole line from the file or an empty string if the file object is at the
  end of the file. How can you tell blank lines? You'll always get back at least a newline
  character like "\n".

* .readlines() - reads all the lines into a list. Sometimes you'll want this.

* .seek() - in case you need to set the position of the file object manually. Eg - if you
  .readlines() twice in a row, the second time you get an empty list because the file object
  remembers its already at the end of the file. But you could call .seek(0) to set the position to
  the beginning of the file.

* .close() - it is important to close a file when done with it. If you kept opening files and never
  closing them you could exhaust the underlying ability of the Operating System to open files. But
  you mostly don't want to call this method either!

Why do I say you often won't be using these methods? Because reading from files is so frequently
used there are some patterns to make it more convenient.

File objects are iterable. Instead of calling .readlines() and looping over the resulting list you
can just loop over the file object. This has the side benefit of not having to load all the lines
of a large file into memory at once!

File objects also support the context management protocol which means you can use the `with`
statement to open a file and it will be automatically closed after the with block. So a common example would be:

>>> with open("../README.md") as f:
...     for line in f:
...         if line.startswith("# "):
...             print(line, end="")
# BeginnerSIG

## You practice!

Write functions that take file names, opens it, and processes the textual data. See the
`sample.txt` file in the same directory.

The data in the sample.txt is actually parsable with Python's `configparser` module - but I want
you to do this with with file objects.

First write a function that returns all the configuration sections in the file (hint: they start with a "[" character). Return a list like:

>>> read_sections("sample.txt")
['security', 'client', 'server']

Now tackle a slightly harder task - read till you find an indicated header than return all the
non-empty lines below it till you come to another header or the end of the file:

>>> read_section("sample.txt", "security")
[('encryption', 'True'), ('allow_anonymous', 'False')]

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
