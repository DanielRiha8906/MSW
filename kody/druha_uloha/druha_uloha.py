import pandas as pd
import matplotlib.pyplot as plt

path = "/home/aerceas/Documents/dev/MSW/kody/data/druha_uloha/Refugees.csv"

df = pd.read_csv(path)

print(df.head())

#########################

df_czech = df[(df['Country...territory.of.asylum.residence'] == 'Czech Rep.') & (df['Year'] >= 1991)]

df_czech_grouped = df_czech.groupby('Year')['Total.Population'].sum()

plt.figure(figsize=(10, 6))
df_czech_grouped.plot()
plt.title('Total Refugees that went to  Czech Republic Over Time (1991 onwards)')
plt.xlabel('Year')
plt.ylabel('Total Refugees')
plt.grid(True)
plt.savefig('total_refugees_czech_over_time.png')
plt.show()

#########################

df_origin_grouped = df.groupby('Origin')['Total.Population'].sum()

top_9_origins = df_origin_grouped.nlargest(9)

rest_sum = df_origin_grouped.sum() - top_9_origins.sum()

other_series = pd.Series({'Other': rest_sum})

top_10 = pd.concat([top_9_origins, other_series])

plt.figure(figsize=(10, 6))
top_10.plot(kind='bar')

plt.title('Top 10 Zemí, které přijali uprchlíky')
plt.xlabel('Země')
plt.ylabel('Počet uprchlíků')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('graf_2.png')
plt.show()

#########################

df_asylum_seekers = df[['Year', 'Asylum.seekers..pending.cases.']]

df_asylum_seekers_grouped = df_asylum_seekers.groupby('Year')['Asylum.seekers..pending.cases.'].sum()

plt.figure(figsize=(10, 6))
df_asylum_seekers_grouped.plot()
plt.title('Asylum Seekers Pending Cases Over Time')
plt.xlabel('Year')
plt.ylabel('Asylum Seekers Pending Cases')
plt.grid(True)
plt.savefig('asylum_seekers_pending_cases_over_time.png')
plt.show()



#########################


df_yearly_population = df.groupby('Year')['Total.Population'].sum()

top_10_years = df_yearly_population.nlargest(10)

plt.figure(figsize=(10, 6))
top_10_years.plot(kind='bar')
plt.title('Top 10 Years by Total Refugees')
plt.xlabel('Year')
plt.ylabel('Total Refugees')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('top_10_years_by_total_refugees.png')
plt.show()

#########################


df_asylum = df.groupby('Country...territory.of.asylum.residence')['Total.Population'].sum()

top_9_asylum_countries = df_asylum.nlargest(9)

rest_sum_asylum = df_asylum.sum() - top_9_asylum_countries.sum()

other_series_asylum = pd.Series({'Other': rest_sum_asylum})

top_10_asylum = pd.concat([top_9_asylum_countries, other_series_asylum])

plt.figure(figsize=(12, 8))
top_10_asylum.plot(kind='bar')
plt.title('Top 10 zemí, ze kterých bylo nejvíce uprchlíků')
plt.xlabel('Země původu')
plt.ylabel('Počet uprchlíků')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('graf_5.png')
plt.show()