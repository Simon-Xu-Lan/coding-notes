- Micro Name

  - Up to 255 Characters
  - No space or special characters (@,! $ #)
  - Don't start the Micro name with number

- Logic

  - if else
    - sequence if else
    - **only the do one option that matches the condition**
    ```VB
      If userInput = "1" Then
        'Do something
      ElseIf useInput = "2" Then
        'Do something else
      Else
        'Do this if the above isn't true
      End if
    ```
    - parallel if else
    - **Will do all options that match the condition**
    ```VB
      If userInput = "1" Then
        'Do something
      end if
      If useInput = "2" Then
        'Do something else
      end if
      if useInput = "3" Then
        'Do this if the above isn't true
      End if
    ```

- MsgBox
- InPutBox

- DO WHILE loop

  ```VB
    Do While ActiveCell.Value <> ""
      'Do something
    Loop
  ```

- DO UNTIL loop

  ```VB
    Do Until ActiveCell.Value = ""
      'Do something
    Loop
  ```

- For loop

  ```VB
    For i = 1 to Worksheets.Count
      WorkSheets(i).Select
      'Do something

    Next i
  ```

  - For i = start to end
  - eg. For i = 1 to 5
  - loop through 1, 2, 3, 4, 5.
  - including both start and end

- last cell

  ```vb
    Dim last_cell As String
    Range("F2").Select
    Selection.End(xlDown).Select
    lastCell = ActiveCell.Address

    ActiveCell.offset(1,0).Select

    ActiveCell.Value = "=SUM(F2:" + lastCell + ")"
    ActiveCell.Font.Bold = True
  ```

- last row

  ```vb
    lastrow = Cells(Rows.Count, 1).End(xlUp).row
  ```

  - "Rows" is a global variable to refer the rows
  - "Rows.Count" is total rows in the worksheet, including all empty rows.
  - "End() is a method
    = "xlUp" is a parameter for end method. it means move up.

- last column

- Cells(x ,y)

  - x is row, start from 1, eg. row 1: x = 1
  - y is col, start from 1, eg. col A: y = 1
  - Cells(x, y).Value
    - The value in the cell of x, y

- count how many sheets in a workbook

  ```VB
    Worksheets.Count
  ```

- range

  ```vb
    dim n as integer
    n=3
    range("H"&n)
    ' the above equals to range("H3")
  ```

- VBA concatenate: &

  ```vb
    "Row" & 5 ' result is Row5
  ```

- VBA format

  ```VB
  ' Set the Font color to Red
  Range("A1").Font.ColorIndex = 3

  ' Set the Cell Colors to Red
  Range("A2:A5").Interior.ColorIndex = 3

  ' Set the Font Color to Green
  Range("B1").Font.ColorIndex = 4

  ' Set the Cell Colors to Green
  Range("B2:B5").Interior.ColorIndex = 4

  ' Set the Color Index to Blue
  Range("C1").Font.ColorIndex = 5

  ' Set the Cell Colors to Blue
  Range("C2:C5").Interior.ColorIndex = 5

  ' Set the Color Index to Magenta
  Range("D1").Font.ColorIndex = 7

  ' Set the Cell Colors to Magenta
  Range("D2:D5").Interior.ColorIndex = 7
  ```

  - See this website for color guides:
    - http://dmcritchie.mvps.org/excel/colors.htm

- worksheet name
  ```VB
    ws.name
  ```

- Insert a column, row
  https://docs.microsoft.com/en-us/office/troubleshoot/excel/macro-insert-delete-rows-columns
 
- Iterate worksheets
  ```VB
    For Each worksheet in worksheets
      ' Do something
    next worksheet
  ```