# f-strings formatter including for loop

```py
  dct = {'a': 1, 'b': 2}
  newline = "\n"  # \escapes are not allowed inside f-strings
  print(f'{newline.join(f"{key}: {value}" for key, value in dct.items())}')
```

- output:
  a: 1
  b: 2

```py
  dct = {'a': 1, 'b': 2}
  newline = "\n"  # \escapes are not allowed inside f-strings
  print("\n".join(f"{key}: {value}" for key, value in dct.items())))
```

- output:
  a: 1
  b: 2

# f-strings formatter including if else

```py
  c, name = "Hello", ""
  result = f'{c} {name if name else "unknown"}'
  print(result)
```

- output:
  Hello unknown
