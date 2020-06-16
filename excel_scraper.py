import pandas as pd
excel_file = 'music_library.xlsx'
library = pd.read_excel(excel_file)

library.head()
