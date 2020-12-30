```py
import pandas

import csv

BACKGROUND_COLOR = "#B1DDC6"
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data_frame.to_dict(orient='records') # convert the data frame into dictionary


# ==== use pandas to write to csv file
    data = pandas.DataFrame(to_learn)
    # index=False means to remove the index while writing into csv file
    data.to_csv("data/words_to_learn.csv", index=False)

    # ==== Use csv to write to csv file
    # Save new to_learn to new file
    with open("data/words_to_learn.csv", "w") as file:
        writer = csv.writer(file)
        # write the column heading for the first row
        writer.writerow(["French", "English"])
        for row in to_learn:

            writer.writerow([row['French'], row['English']])
```

**Dictionary comprehension template for pandas DataFrame:**

```py
  new_dict = {new_key: new_value for (index, dataframe_row) in dataframe.iterrows()}
```
