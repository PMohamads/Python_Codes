import pandas as pd

veri = pd.read_csv("iris.data")
print(veri.head())
#print(veri.sample)
print(veri.columns)
print(veri[3:5])

veri = veri.sort_values(by="sepal_length")
print(veri.head())
"""print(veri.sort_values(by="sepal_length"))"""

toplam_veri = veri["sepal_length"].sum()
ortalam_veri = veri["sepal_length"].mean()
ortanca_veri = veri["sepal_length"].median()

print("sum : ", toplam_veri)
print("mean : ", ortalam_veri)
print("median : ", ortanca_veri)
