import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

df = pd.read_excel("processed_cars.csv")

plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title("Car Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df['year'], y=df['price'])
plt.title("Price vs Car Manufacturing Year")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df['km_driven'], y=df['price'])
plt.title("Price vs KM Driven")
plt.xlabel("Kilometers Driven")
plt.ylabel("Price")
plt.show()

if "brand" in df.columns:
    brand_avg = df.groupby("brand")["price"].mean().sort_values(ascending=False).head(20)
    plt.figure(figsize=(10,6))
    brand_avg.plot(kind='bar')
    plt.title("Top 20 Brands with Highest Average Price")
    plt.xlabel("Brand")
    plt.ylabel("Average Price")
    plt.xticks(rotation=45)
    plt.show()

if "fuel" in df.columns:
    plt.figure(figsize=(8,5))
    df['fuel'].value_counts().plot(kind='bar')
    plt.title("Fuel Type Distribution")
    plt.xlabel("Fuel Type")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.show()

if "owner_count" in df.columns:
    plt.figure(figsize=(8,5))
    df['owner_count'].value_counts().sort_index().plot(kind='bar')
    plt.title("Owner Count Distribution")
    plt.xlabel("Number of Owners")
    plt.ylabel("Count")
    plt.show()

print("All graphs generated successfully!")
