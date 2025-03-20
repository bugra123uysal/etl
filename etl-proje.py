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
aa['house-room']=aa[['bedrooms','bathrooms','guestroom']].sum(axis=1) 
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

# 📊 1. Mobilya Durumu ve Ortalama Fiyat (Barplot)
plt.figure(figsize=(8,5))
sns.barplot(x=aa['furnishingstatus'], y=aa['price'], data=aa)
plt.title("Mobilya Durumu ve Ortalama Fiyat", fontsize=14)
plt.xlabel("Mobilya Durumu", fontsize=12)
plt.ylabel("Ortalama Fiyat", fontsize=12)
plt.show()

# 📊 2. Fiyat ve Alan İlişkisi (Scatter Plot)
plt.figure(figsize=(8,6))
sns.scatterplot(x=aa['price'], y=aa['area'], size=aa['lux']/aa['lux'].max(), hue=aa['furnishingstatus'])
plt.title("Fiyat ve Alan İlişkisi", fontsize=14)
plt.xlabel("Fiyat", fontsize=12)
plt.ylabel("Alan (m²)", fontsize=12)
plt.show()

# 📊 3. Yatak Odası Sayısı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['bedrooms'], data=aa)
plt.title("Yatak Odası Sayısı Dağılımı", fontsize=14)
plt.xlabel("Yatak Odası Sayısı", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 4. Banyo Sayısı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['bathrooms'], data=aa)
plt.title("Banyo Sayısı Dağılımı", fontsize=14)
plt.xlabel("Banyo Sayısı", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 5. Ana Yola Yakınlık (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['mainroad'], data=aa)
plt.title("Ana Yola Yakınlık", fontsize=14)
plt.xlabel("Ana Yola Yakın mı?", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 6. Kat Sayısı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['stories'], data=aa)
plt.title("Kat Sayısı Dağılımı", fontsize=14)
plt.xlabel("Kat Sayısı", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 7. Toplam Oda Sayısı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['house-room'], data=aa)
plt.title("Toplam Oda Sayısı Dağılımı", fontsize=14)
plt.xlabel("Oda Sayısı", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 8. Bodrum Katı Olan Evlerin Dağılımı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['basement'], data=aa)
plt.title("Bodrum Katı Olan Evler", fontsize=14)
plt.xlabel("Bodrum Katı Var mı?", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 9. Öncelikli Bölgeye Göre Ev Sayısı (Countplot)
plt.figure(figsize=(8,5))
sns.countplot(x=aa['prefarea'], data=aa)
plt.title("Öncelikli Bölgeye Göre Ev Sayısı", fontsize=14)
plt.xlabel("Öncelikli Bölge (Evet/Hayır)", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 10. Lüks Seviyesi ve Fiyat Dağılımı (Boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(x=aa['lux'], y=aa['price'])
plt.title("Lüks Seviyesi ve Fiyat Dağılımı", fontsize=14)
plt.xlabel("Lüks Puanı", fontsize=12)
plt.ylabel("Fiyat", fontsize=12)
plt.show()

# 📊 11. Ortalama Oda Büyüklüğü ve Fiyat Dağılımı (Boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(y=aa['price'], x=aa['house-room'])
plt.title("Oda Sayısına Göre Fiyat Dağılımı", fontsize=14)
plt.xlabel("Oda Sayısı", fontsize=12)
plt.ylabel("Fiyat", fontsize=12)
plt.show()

# 📊 12. Ev Fiyatlarının Dağılımı (Histogram)
plt.figure(figsize=(10,6))
sns.histplot(aa['price'], bins=30, kde=True)
plt.title("Ev Fiyatlarının Dağılımı", fontsize=14)
plt.xlabel("Fiyat", fontsize=12)
plt.ylabel("Ev Sayısı", fontsize=12)
plt.show()

# 📊 13. Otopark Sayısına Göre Ortalama Fiyat (Barplot)
plt.figure(figsize=(8,5))
sns.barplot(x=aa['parking'], y=aa['price'], data=aa)
plt.title("Otopark Sayısına Göre Ortalama Fiyat", fontsize=14)
plt.xlabel("Otopark Sayısı", fontsize=12)
plt.ylabel("Ortalama Fiyat", fontsize=12)
plt.show()

print(aa.columns)