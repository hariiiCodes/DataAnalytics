import pandas as pd
# data={'Name':['Asha','Ravi','John'],'Age':[22,25,23]}
# df=pd.DataFrame(data)
# print(df)

# s=pd.Series([10,20,30])
# print(s)
# x=pd.Series([10,20,30],index=['a','b','c'])
# print(s)
csv_data=pd.read_csv("sample.csv",encoding="latin1")
excel_data=pd.read_excel("sample.xlsx")
json_data=pd.read_json("sample.json")


print("CSV Successfull!")
print(csv_data.tail())

print("------------------------------------------------------------")


print("EXCEL Successfull!")
print(excel_data.head())

print("------------------------------------------------------------")


print("JSON Successfull!")
print(json_data.head())



