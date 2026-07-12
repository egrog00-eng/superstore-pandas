import pandas as pd

df = pd.read_csv("train.csv")

# базовая информация и проверка на null и повторки

print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())

# в датасете эти колонки являются форматом object, поэтому меняем их на формат дд/мм/гггг

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")

print(df.dtypes)

# смотрим диапазон дат

print(df["Order Date"].min())
print(df["Order Date"].max())

# топ 10 заказов по сумме продаж

print(df.sort_values("Sales", ascending=False).head(10))

# считаем общие продажи по каждой категории

print(df.groupby("Category")["Sales"].sum())

# выбираем год как отдельную колонку

df["Order Year"] = df["Order Date"].dt.year

# анализ продаж за 2018 год

print(df[df["Order Year"] == 2018].head())
print(df[df["Order Year"] == 2018].groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))

# продажи по регионам

print(df.groupby("Region")["Sales"].agg(["sum", "mean", "count"]))

# базовая информация

print(df.describe())

# считаем время доставки в днях и среднее время доставки по каждому виду транспортировки

df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
print(df[['Order Date', 'Ship Date', 'Delivery Days']].head())
print(df.groupby('Ship Mode')['Delivery Days'].mean())

# топ 10 покупателей по их сумме покупок

print(df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10))

# сводная таблица продаж по категории и региону

pivot = pd.pivot_table(df, values='Sales', index='Category', columns='Region', aggfunc='sum')
print(pivot)
pivot.to_csv('category_region.csv')