import pyodbc  
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



aa=pd.read_csv("C:\\Users\\buğra\\Desktop\\Housing.csv")

print(aa.isnull().sum())

print(aa.head())



print(aa.tail())
print(aa.info())



print(aa['parking'])
print(aa.describe())

aa.replace({"yes":1 ,"no":0},inplace=True)
print((aa==0).sum())


aa['price_per_sqft']=aa['price'] / aa['area']

aa['stories-area']=aa['area'] / aa['stories']
aa['lux']= aa[['guestroom', 'hotwaterheating', 'airconditioning', 'prefarea','mainroad','basement']].sum(axis=1)
aa['prefarea_effect']=aa['prefarea'] * aa['price']
aa['parking_bedroom']= aa['parking'] / aa['bedrooms']
print(aa.head())