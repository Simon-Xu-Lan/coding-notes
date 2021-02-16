- range()

  - range(5, 0, -1)
    - start: 5
    - stop: 0
    - step: -1
    - it will go: 5, 4, 3, 2, 1, 0

- slicer

  - works for both list and tuple
  - piano_keys = [0,1,2,3,4,5,6,7]
  - piano_keys[2:5] = [2,3,4]
  - ![python slicer]()
  - piano_keys[2:5:2] = [2,4]
    - the last number 2 is step
  - piano_keys[2:] = [2,3,4,5,6,7]

  - reverse list
    - piano_keys[::-1] = [7,6,5,4,3,2,1]
  - piano_keys[::2] = [1, 3, 5, 7]

- bool()

  - bool('No') -> True
  - bool('') -> False
  - bool('0') -> True
  - bool(0) -> False

- file methods

  - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# File path

- absolute file path
  - always start from the root foler
  - eg.
    - /work/project/report.ppt
- relative file path
  - from the working folder
  - ./project/report.ppt
  - ./ : current foldeer
  - ../ : pareent folder. one level up
    - The .. goes up one folder
  - if in the same folder
    - the following solutions both works
      - ./report.ppt
      - report.ppt
      - the "./" is optional.
- len()

  - len() is a global method
  - len() method can use not only list but also other classes or object, such as tuple, dictionary ...
  - that is why put list object inside ()
    - len(my_list)

- pop([i])

  - [] means the argument is optional
  - pop() means remove the first element

- instance and object

  - understand it as the same thing

- range(5)

  - 0, 1, 2, 3, 4
  - start from zero by default
  - stop before the spedific number: 5.
  - range(start, stop, step)
    - start optional, default is 0
    - stop required
    - step optional, default is 1
  - range(5,0,-1)
    - 5,4,3,2,1
  - range() is a global method

- os

  - os.path

    - create a file paths across operating system
    - eg.

    ```python
      path = os.path.join('..', 'Resources', 'accounting.csv')
      # result: ../Resources/accounting.scv for OS
      windows: ..//Resources//accounting.scv
      mac OS: ../Resources/accounting.scv
    ```

  - os.chdir("path")

- csv

  - CSV file reading and writing

  ```py
    with open(csvpath) as csvfile:
      # CSV reader specifies delimiter and variable that holds the contents
      csvreader = csv.reader(csvfile, delimiter=",")

      print(CSV ra)
  ```

- csv.writer()

  - if the file "new.csv" doesn't exist, csv.writer() will create the "new.csv" file at current path.
  - if the file "new.csv" exists, csv.writerow would overwrite the old content in new.csv file
    - because the open method use "w" as argument.
  - if open method use "a" as an argument, csv.writerow() would append new contend to the end of old content in new.csv file.

  ```py
    with open("new.csv", 'w', newline='') as csvfile:
      # Initialize csv.writer
      csvwriter = csv.writer(csvfile, delimiter=',')
      # Write the first row (column headers)
      zyjkm    csvwriter.writerow(['First Name1', 'Last Name1', 'SSN1'])
      # Write the second row
      csvwriter.writerow(['Caleb1', 'Frost1', '505-80-29011'])
  ```

  - newline

    - When writing output to the stream, if newline is None, any '\n' characters written are translated to the system default line separator, os.linesep.
    - If newline is '' or '\n', no translation takes place.

  - with open() block
    - with open() block will automatically close file after the block.

- windows os add: csvfile=open(csvpath, encoding='utf8') to solve issue if have

- read() vs. csv.reader()
  - plain reading method read() returns a string
    ```py
      lines = file_handler.read()
    ```

# print(lines)

      # output:
        Tina,Fleming,619-16-7988
        Erica,Shah,164-51-7615
        Paula,Ortiz,051-83-3290
        James,Hendricks,776-83-2884
        Lauren,King,197-94-2398
        David,Cowan,252-92-1832
        Andrew,Burton,296-23-6842
        Julian,Baker,337-40-7543
        Scott,Castro,399-46-5595
        Billy,Rodriguez,014-18-2503
        Darrell,Leblanc,005-82-7918
        David,Hammond,561-17-6312
    ```

- Improved reading method csv.reader() returns a \_csv.reader object,
  - which includs a list of list
  ```py
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # output:
    # <_csv.reader object at 0x7fca5016c7b0>
    for attr in csvreader:
      print(attr)
    # output:
    ['First Name', 'Last Name', 'SSN']
    ['Tina', 'Fleming', '619-16-7988']
    ['Erica', 'Shah', '164-51-7615']
    ['Paula', 'Ortiz', '051-83-3290']
    ['James', 'Hendricks', '776-83-2884']
    ['Lauren', 'King', '197-94-2398']
    ['David', 'Cowan', '252-92-1832']
    ['Andrew', 'Burton', '296-23-6842']
    ['Julian', 'Baker', '337-40-7543']
    ['Scott', 'Castro', '399-46-5595']
    ['Billy', 'Rodriguez', '014-18-2503']
    ['Darrell', 'Leblanc', '005-82-7918']
    ['David', 'Hammond', '561-17-6312']
  ```
- List comprehension

  ```py
   new_list = [new_item for item in list]
  ```

  - the same as the following syntax

  ```py
    new_list = []
    for item in list:
      new_item = ...
      new_list.append(new_item)
  ```

  - with if
    ```py
    [new_item for item in list if test]
    ```
  - get common parts for two list
    ```py
      list1 = [3,6,5,8,33,12,7,4,72,2,42,13]
      list2 = [3,6,13,5,7,89,12,3,33,34,1,344,42]
      commons = [ num for num in list1 if num in list2]
    ```

- Dictionary Comprehension

  ```py
    new_dict = { new_key: new_value for item in list}
    new_dict = { new_key: new_value for (key, value) in dict.items()}
    # for pandas dataframe
    new_dict = {new_key: new_value for (index, dataframe_row) in dataframe.iterrows()}

  ```

- f string comprehension

  ```py
    [f"Headline: {article['title']}. \nBreif: {article['description']}" for article in articles]

  ```

- pandas

  - Loop through columns for a data frame

  ```py
    for (key, value) in student_data_frame.items():
  ```

  - Loop through rows of a data frame

  ```py
    for (index, row) in student_data_frame.iterrows():
  ```

  - Read csv file
  - csv file:
    letter,code
    A,Alfa
    B,Bravo
    C,Charlie
    D,Delta
    E,Echo
    F,Foxtrot
  - pandas.read-csv

  ```py
    data = pandas.read_csv("csv_file.csv")
    print(data)
  ```

  - result
    letter code
    0 A Alfa
    1 B Bravo
    2 C Charlie
    3 D Delta
    4 E Echo
    5 F Foxtrot
  - to_dict()

    ```py
      data = pandas.read_csv("csv_file.csv").to_dict()
      print(data)
    ```

    - result:
      {
      'letter': {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'},
      'code': {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot'}
      }

  - ```py
      dict = {row.letter: row.code for (index, row) in data.iterrows()}
      # or dict = {row[0]: row[1] for (index, row) in data.iterrows()}
      print(dict)
    ```

    - result:
      {
      'A': 'Alfa',
      'B': 'Bravo',
      'C': 'Charlie',
      'D': 'Delta',
      'E': 'Echo',
      'F': 'Foxtrot'
      }

- pandas excel

  ```py
    sheet1 = pandas.read_excel(excel_file, sheet_name='Sheet1')
    print(sheet.head(10))
    sheet1["column header name"] # pull the column
    sheet1.insert(0, "First Name", first_name_list) # insert the column in the first postion, data source: first_name_list.
    del sheet1['First Name, Last Name'] # delete the 'First Name, Last Name' column

    Important_numbers = sheet1['Important Number']  # Get the column of 'Important Number'
    pandas.to_numeric(Important_numbers) # Change it to number
    Edited_Important_numbers = Important_numbers * 2
    sheet1['Important Number'] = Edited_Important_numbers # replace the column

    sheet1.to_excel("output.xlsx")  # save back to excel file


  ```

  - reading multiple sheets
    - In this example we are going to read two sheets, 'Session1' and 'Session2'.
    - If you have more sheets, you can add them to the list (parameter sheet_name, is used to specify sheets).

  ```py
    import pandas as pd
    sheets = pd.read_excel('example_sheets2.xlsx', sheet_name=['Session1', 'Session2'])
    # sheets output:
      OrderedDict([
        (
          'Session1',  Name  ID  Mean  Correct  Session
              0       Pete   1    32       15        1
              1      Steve   2    31       14        1
              2       Dave   3    30       15        1
              3    Justine   4    31       13        1
              4   Frederic   5    45       14        1
              5       John   6    99       99        1
              6  Josephine   7    29       11        1
              7        Lee   8    35       14        1
              8      Roman   9    37       14        1
              9   Caroline  10    33       14        1
        ),
        (
          'Session2', Name  ID  Mean  Correct  Session
              0       Pete   1  31.0     14.0        2
              1      Steve   2  32.0     15.0        2
              2       Dave   3  29.0     14.0        2
              3    Justine   4  28.0     12.0        2
              4   Frederic   5  43.0      2.0        2
              5       John   6   NaN      NaN        2
              6  Josephine   7  31.0     11.0        2
              7        Lee   8  33.0     13.0        2
              8      Roman   9  38.0     15.0        2
              9   Caroline  10  33.0     14.0        2
        )
      ])
    # real all sheets
    sheet_to_df_map = pd.read_excel('example_sheets2.xlsx', sheet_name=None)
    # join the data from all sheets
    df = pd.concat(sheet_to_df_map[frame] for frame in sheet_to_df_map.keys())
    # sheet_to_df_map: https://github.com/marsja/jupyter/blob/master/Reading%20Multiple%20Spreadsheets%20using%20Pandas.ipynb

    # write into different worksheets
    df1 = pd.DataFrame({'Names': ['Andreas', 'George', 'Steve',
                         'Sarah', 'Joanna', 'Hanna'],
                 'Age':[21, 22, 20, 19, 18, 23]})
    df2 = pd.DataFrame({'Names': ['Pete', 'Jordan', 'Gustaf',
                              'Sophie', 'Sally', 'Simone'],
                      'Age':[22, 21, 19, 19, 29, 21]})
    df3 = pd.DataFrame({'Names': ['Ulrich', 'Donald', 'Jon',
                              'Jessica', 'Elisabeth', 'Diana'],
                      'Age':[21, 21, 20, 19, 19, 22]})

    dfs = {'Group1':df1, 'Group2':df2, 'Group3':df3}

    writer = pd.ExcelWriter('NamesAndAges.xlsx', engine='xlsxwriter')
    for sheet_name in dfs.keys():
        dfs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
  ```

- openpyxl

  ```py
    wb = openpyxl..load_workbook("filepath")
    type(wb)
    # <CLASS 'openpyxl.workbook.workbook.Workbook'>
    wb.get_sheet_names()
    # ['Sheet1', 'Sheet2', 'Sheet3']
    sheet = wb.get_sheet_by_name('Sheet1')
    type(sheet)
    # <CLASS 'openpyxl.worksheet.worksheet.Worksheet'>
    sheet['A1'].value
    wb.save('filepath') # save to file
    sheet.title
    # 'Sheet1'
    sheet.cell(row=1, column=3).value
    # row start at 1 not 0
    sheet.max_row # find how many rows
    sheet.max_column # find how many columns
    openpyxl.cell.get_column_letter(1) # 1
    openpyxl.cell.column_index_from_string("AA") # 27
    wb.create_sheet(title="my sheet name", index=1) # insert a new sheet, put it at first
    wb.create_sheet("my sheet name")
    sheet.row_dimensions[1].height # set the row height
    sheet.column_dimensions['B'].width = 20 # set the column width
    from "openxyl.styles" import Font
    sheet['B1'].font = Font(sz=14, bold=True, italic=True)

    wb = openpyxl.Workbook() # open a new workbook
    sheet["A" + i].value
    sheet['C8'].value = '=SUM(C1:C7)'  # Handle formula


  ```

  - .load_workbook("filepath")
    - <CLASS 'openpyxl.workbook.workbook.Workbook'>

- advance arguments
- Keyword Arguments
  ```py
    def my_function(a, b, c)
    my_function(c=3, a=1, b=2)
  ```
  - Arguments with Default Values
  ```py
    def my_function(a=1, b=2, c=3)
    # 1, 2, 3 are default values
    # use default values like this
    my_function() # a, b, c use default value
    my_function(b=5) #a,c use default value, b uses 5
    my_funtion(4,9)  # only c get a default value, a use 4, b use 9
  ```
- Unlimited Arguments

  ```py
    def add(*arg)
    # * is required, arg can be any word you can use.
    # arg is a tuple
    # can access by index, eg. arg[0], arg[i]

  ```

- Key word argument

  - \*args: Unlimited Positional Arguments
  - \*\*kw: Unlimited Keyword Arguments

  ```py
  # **kwarg -- unlimited keyword argument
  # **kw
  # argument is a dictionary
  # give us a flexibility to work with argument
  # give us a way to name the argument
  class Car:

    def __init__(sefl, **kw):
      self.make = kw["make"]
      self.model = kw["model"]
      # get method, if key doesn't exit, it wont' get error, just return none.
      self.model= kw.get("model")

    # eg.
    def all_aboard(a, *args, **kw):
    print(a, args, kw)

    all_aboard(4, 7, 3, 0, x=10, y=64)
    # output:
    4 (7,3,0) {'x': 10, 'y': 64}
    # 4 is passed by position. 7,3,0 are collected into a tuple. x and y are in a keyword dictionary
  ```

- copy and paste

  - "pyperclip" package

- Errors, Exceptions

  - rule:
    - **Use error exception method only if you can not easily do if else.**
  - try:
    - Something that might cause an exception
  - except:
    - Do this there was an exception
  - else:
    - Do this if there were no exception
  - finally:
    - Do this no matter what happens
  - eg.
    - https://www.udemy.com/course/100-days-of-code/learn/lecture/20963160#questions
      - lecture: 268
  - raise error

- JSON Data

  - Wrtie
    - json.dump()
  - Read
    - json.load()
  - Update
    - json.update()

- Run the code every 60 seconds.

```py
  import time

  while True:
    time.sleep(60)
    # do something
```

- html module

  - html.unescape()
  - HTML Symbols
    - https://www.w3schools.com/html/html_symbols.asp

- Type Hint and Arrows ->

```py
  age: int
  name: str
  height: float
  is_human: bool

  def police_check(age: int) -> bool:
    if age > 18:
      can_drive = True
    else:
      can_drive = False
    return can_drive  # return value must be bool as defined.
```

- slice list

```py
  a[start: stop] # items start through stop-1
  a[start:]      # itesm start through the rest of the array
  a[:stop]       # items start the beginning through stop-1
  a[:]           # a copy of the whole array
  a[::-1]        # reverse the list
    a.reverse()
    for n in range(len(a)-1, 0, -1):
```

# jupyter

- launch jupyter notebook
- at terminal under a folder, run "jupyter notebook"

  - the jupyter will serve that folder
  - automatically open that folder on browser

- run cell: shift + enter

When cell is under editing, it is highlighted by green
When cell is highlighted by blue, you can change the mode

- press "m" key for markdown mode, cell is highlighted by blue
- press "y" key for code mode, cell is highlighted by green

# Python Decorators

## Functions can have inputs/functionality/output

```py
  def add(n1, n2):
      return n1 + n2

  def subtract(n1, n2):
      return n1 - n2

  def multiply(n1, n2):
      return n1 * n2

  def divide(n1, n2):
      return n1 / n2
```

## Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

````py
  def calculate(calc_function, n1, n2):
      return calc_function(n1, n2)

  result = calculate(add, 2, 3)
print(result)
# Output: 5
``
## Functions can be nested in other functions
```py
  def outer_function():
      print("I'm outer")

      def nested_function():
          print("I'm inner")

      nested_function()

  outer_function()
  # Output:
  # I'm outer
  # I'm inner
````

## Functions can be returned from other functions

```py
  def outer_function():
      print("I'm outer")

      def nested_function():
          print("I'm inner")

      return nested_function

  inner_function = outer_function()
  inner_function()
  # Output:
  # I'm outer
  # I'm inner
```

# Python decorator function

## Python decorator function is a function which wrap another function and give it additional functionality or modify the functionality

## Simple Python Decorator Functions

```py
  import time

  def delay_decorator(function):
    def wrapper_function():
      time.sleep(2)
      #Do something before
      function()
      function()
      #Do something after
    return wrapper_function

  # With @ syntactic suger
  @delay_decorator
  def say_hello():
  print("Hello")

  #With the @ syntactic sugar
  @delay_decorator
  def say_bye():
  print("Bye")

  #Without the @ syntactic sugar
  def say_greeting():
  print("How are you?")
  decorated_function = delay_decorator(say_greeting)
  decorated_function()
```

# Visualize Coding Running

- http://pythontutor.com/visualize.html#mode=display

# Class

- Day 17

# Continue and break

- Continue 会跳过当前层循环中的代码，强迫执行当前层的下一次循环
- Break 是用来终止当前的循环， 但是并不终止外层循环。
