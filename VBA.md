- Micro Name

  - Up to 255 Characters
  - No space or special characters (@,! $ #)
  - Don't start the Micro name with number

- Logic

  - if else

  ```VB
    If userInput = "1" Then
      'Do something
    ElseIf useInput = "2" Then
      'Do something else
    Else
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

- Cells.(x ,y)
  - x is row, start from 1, eg. row 1: x = 1
  - y is col, start from 1, eg. col A: y = 1
