import pandas as pd
# data={'Name':['Asha','Ravi','John'],'Age':[22,25,23]}
# df=pd.DataFrame(data)
# print(df)

# s=pd.Series([10,20,30])
# print(s)
# x=pd.Series([10,20,30],index=['a','b','c'])
# print(s)
df=pd.read_csv(r"C:\Users\admin\Downloads\player_stats.csv")
print(df.head())
