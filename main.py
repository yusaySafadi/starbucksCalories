import tabula
import pandas as pd
tables = tabula.read_pdf("AUT23_Naehrwertinfos_Beverages.pdf",pages="all")

merged_table = pd.concat(tables, ignore_index=True)

print(tables)