import pyodbc  
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



aa=pd.read_csv(r"C:/Users\buğra/Desktop/Housing.csv")

print(aa.isnull().sum())

print(aa.head())



"""print(aa.tail())
print(aa.isnull().sum())
print(aa['parking'])
print(aa.describe())
print(aa.info())
  """
 


aa.replace({"yes":1 ,"no":0},inplace=True)
print((aa==0).sum())

""" Evin fiyatının metrekare başına maliyetini hesaplamak için  """
aa['price_per_sqft']=aa['price'] / aa['area']
""" Evin kat başına düşen alanı hesaplamak  """
aa['stories-area']=aa['area'] / aa['stories']
aa['house-room']=aa[['bedrooms','bathrooms']].sum(axis=1) 
""" Böylece evlerin donanım seviyesini ölçen bir yeni değişken  """
aa['lux']= aa[['guestroom', 'hotwaterheating', 'airconditioning', 'prefarea','mainroad','basement']].sum(axis=1)
""" Büyük evlerin yeterince otoparkı var mı? """
aa['parking_bedroom']= aa['parking'] / aa['bedrooms']
aa['bedrooms-price']=aa['price'] /aa['bedrooms']

""" ortalama oda büyüklüğü """
aa['average-room-size']=aa['area']/ aa['house-room']
""" Fiyatın oda sayısına """
aa['price-room']=aa['price']/ aa['house-room']




aa.to_csv('C:/Users/buğra/Desktop/Housing.csv', index=False)
print("csv dosyası indirildi")



sns.barplot(y=aa['price'] , hue=aa['furnishingstatus'], data=aa)
plt.title("sa")
plt.show()


sns.scatterplot(x=aa['price'], y=aa['area'], size=aa['lux'], hue=aa['furnishingstatus' ]  , data=aa)
plt.show()

sns.countplot(x=aa['bedrooms'], data=aa )
plt.title('bedrooms count')
plt.show()

sns.countplot(x=aa['bathrooms'], data=aa)
plt.title('bathrooms count')
plt.show()

sns.countplot(x=aa['mainroad'], data=aa)
plt.title('mainroad count')
plt.show()

sns.countplot(x=aa['stories'] ,data=aa )
plt.title('stories count')
plt.show()


sns.countplot(x=aa['house-room'] ,data=aa )
plt.title('house-room count')
plt.show()

sns.countplot(x=aa['basement'] ,data=aa )
plt.title('basement count')
plt.show()


sns.countplot(x=aa['prefarea'] ,data=aa )
plt.title('prefarea count')
plt.show()



print(aa.columns)