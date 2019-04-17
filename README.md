# BeginnerSIG

This repo contains Python exercises used by the Beginner Special Interest Group meeting at SF Python Meetup.

## How do I get started learning Python?

There are a few pre-steps!

1. Pick a partner! You can work on your own but while you're at the meetup find somebody to co-work with. I encourage you
   to alternate who types but work together to complete each exercise. Talk through the problem and solutions before you write any code!
2. You need a Python installation on your computer - preferably Python 3.6 or greater. TODO: How to work via PythonAnywhere.
3. Clone this repo using git or download it as a zip file and extract it to your machine so you have all the files.

Now that you're setup it's time to work through the exercises. To do so you only need 3 steps.

1. Pick an area you want to learn about from the table of contents immediately below. If you
   haven't completed any of the exercises be sure to try the *Getting Started* lesson first.
2. Once you've picked your exercise, open the named file in your coding editor of choice and read
   it without making any changes. The exercise consists of explanations and sample code (tests)
   that can be run. Some of the samples won't work and it's your job to add new code to the
   file that will make the tests pass.
3. Run the tests! Each file will have instructions at the top but in general you can run the tests
   simply by running the file.
4. Pick the first failing test and make it pass by adding code. Test your work by returning to step
   3 - you should see one less failing test or a helpful error message explaining what you've still
   got wrong. When you see no failing tests - you've completed the exercise.

Did you get stuck somewhere? Be sure to cheat by peeking at the completion file which has the same
name + "completion". You can run this file to prove it works and read it to see some example solutions.

TODO: Screencast video of completion of an exercise.

## Available Exercises

### Getting Started

* `getting_started/getting_started.py` - Do this first to understand how the exercises work!
* `getting_started/basic_functions.py` - If you don't know what a function is, do this next. You'll
  need to know about functions to complete any of the other exercises.

### Basic logic

* `basic_logic/operators_and_if.py` - This is a chance to get familiarity with some of the punctuation in Python especially as it applies to numbers and strings.
* `indexing.py` - Step through arrays (and strings which are arrays of characters) forwards, backwards, and understand unique quirks related to indexing in Python.
* `looping_and_iteration.py` - Practice using loops (for, while, for x in y) and iterating through them.

### Strings
* `strings/string_manipulation.py` - Learn more about strings and the many methods often used when working with strings.

### Intermediate
* `args_and_kwargs.py` - Learn how to create functions that can handle multiple data types for the same input.

## How do I contribute to this repo?

Please help flesh out the documentation, explaining (or pointing to good documentation) how to edit
files, run them with python, read test output, etc.

Feel free to add additional areas or exercises. Please be sure to copy the style of existing exercises. In particular:

1. Exercises are defined by a single files with a docstring containing doctests. Exercises should contain as much explanation as tests.
2. Provide an `if __name__ == '__main__'` block that invokes doctest. Running the file should run the tests.
3. Be sure to have block comments defining the editable region of the file.
4. Provide a `_completion.py` file which demonstrates the solutions.
