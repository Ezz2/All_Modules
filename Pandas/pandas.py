# By Ezz

import pandas as pd

''' There Are Two Types Of Pandas
[1] Pandas Series
[2] Pandas DataFrame
'''

# Series
ls1 = ["Ahmed", "Mohamed", "Ali", "Hassan", "Tarek", "Ibrahim", "Khaled"]
ls2 = [10, 20, 30, 40, 50, 60, 70]

ser1 = pd.Series(ls1)
ser2 = pd.Series(ls2)

print(ser1)
print(ser2)

ser3 = pd.Series(ls1, index=["a", "b", "c", "d", "e", "f", "g"])

print(ser3)
