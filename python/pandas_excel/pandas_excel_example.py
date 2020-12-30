import pandas as pd

sheets = pd.read_excel("nov production.xlsx", sheet_name=['painting'])
print(sheets)