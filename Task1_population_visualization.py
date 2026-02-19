import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)
df_2022=df[['Country Name','2022']].dropna()

plt.figure(figsize=(8,5))
sns.histplot(df_2022['2022'], bins=20, kde=True)

plt.title("Distribution of Population Across Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.savefig("histogram_population.png")
plt.show()

top10 = df_2022.sort_values(by='2022', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='Country Name', y='2022', data=top10)

plt.xticks(rotation=45)
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.savefig("top10_population.png")
plt.show()