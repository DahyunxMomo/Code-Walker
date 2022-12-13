import pandas as pd
import qrcode as qr

df = pd.read_excel(r"C:\Users\thehi\Desktop\CODE\PandasExcel\Excel.xlsx")
print(df)

data = df
img = qr.make(data)
img.save('prueba.png')