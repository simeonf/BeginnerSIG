"""# CSV Data

You know what Comma Separated Data is, right? A very simple plain-text format
where data is separated by commas, string data that might contain commas is
quoted, and typically the first line contains the column headings.

Something like:

    month, number_occurences
    Jan, 10
    Feb, 8
    Mar, 190

and so on. See the somewhat more complicated .csv file in this directory sourced
from https://catalog.data.gov/dataset/film-locations-in-san-francisco-b217a for
an example of a more realistic csv data file.

## Python support for CSV

You could read that file with python code, break apart each string by commas,
strip off the newlines and process the data. But what about associating columsn
with their names? And what about quoted columns that contain commas in the data?

Fortunately Python has a builtin csv module to make reading csv data really
trivial. Given a source of csv data:

>>> data = ["red,green,blue", "1,2,3", "4,5,6"]

We can import the csv module and make a "reader".

>>> import csv
>>> reader = csv.DictReader(data)

Typically we loop over that reader in a for loop to read all the lines but
we can read the next row with the `next` function:

>>> row = next(reader)
>>> row
OrderedDict([('red', '1'), ('green', '2'), ('blue', '3')])

Notice that the DictReader assumes the first row in the data will be column names and uses that row
to build a dictionary out of the first row of data. Now that we have a row which has dictionary
behavior it's easy to retrieve the value for a column name:

>>> row['red']
'1'

## You do it!

I'll handle opening the file - you write some code to answer questions based on the data in the file.

>>> with open("./Film_Locations_in_San_Francisco.csv") as csv_file:
...     count_lines(csv_file)
1622

*Hint* The reader doesn't have any methods defined to count the number of rows. You may want to
convert to some container that knows about the number of items it contains.

>>> with open("./Film_Locations_in_San_Francisco.csv") as csv_file:
...     count_films_in_2016(csv_file, 2016)
168

*Hint* The reader doesn't do type conversion - all data read from a text file is a string, even if
that string contains data that could be interpreted numerically. And it doesn't have any methods
for searching or querying - you'll want to loop over the data or convert to a container that can be
searched.

# Running the exercises

In order to run these snippets automatically you could go to your terminal environment (eg
Terminal.app on Mac) and run the following command (everything after the "$")

$ python read_csv.py

You should see a report of successes and failures.

To make the failing tests pass, add your own Python code or edit the partial completions in the
space below.

"""

import csv

# DO NOT EDIT ABOVE THIS LINE
# Add (or edit) python code below this comment block


# DO NOT EDIT BELOW THIS LINE
# Add (or edit) python code above this comment block

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if results.failed == 0:
        print("Success! All exercises passed!")
