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
  - piano_keys[::-1] = [7,6,5,4,3,2,1]
  - reverse the list
  - piano_keys[::2] = [1, 3, 5, 7]

- bool()

  - bool('No') -> True
  - bool('') -> False
  - bool('0') -> True
  - bool(0) -> False

- file methods

  - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

- Filt path
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

- os.path

  - create a file paths across operating system
  - eg.

  ```python
    path = os.path.join('..', 'Resources', 'accounting.csv')
    # result: ../Resources/accounting.scv for OS
    windows: ..//Resources//accounting.scv
    mac OS: ../Resources/accounting.scv
  ```

- csv

  - CSV file reading and writing

  ```py
    with open(csvpath) as csvfile:
      # CSV reader specifies delimiter and variable that holds the contents
      csvreader = csv.reader(csvfile, delimiter=",")

      print(CSV ra)
  ```
