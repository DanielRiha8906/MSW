import pandas as pd
import matplotlib.pyplot as plt

path = "/home/aerceas/Documents/dev/MSW/kody/data/druha_uloha/Refugees.csv"

df = pd.read_csv(path)

# Print the first few rows of the DataFrame to confirm it has been read correctly
print(df.head())

df_czech = df[(df['Country...territory.of.asylum.residence'] == 'Czech Rep.') & (df['Year'] >= 1991)]

# Group by year and sum the total population
df_czech_grouped = df_czech.groupby('Year')['Total.Population'].sum()

# Example 1: Line Plot - Total refugees from Czech Rep. over time (starting from 1991)
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

# Sort the values and get the top 9 origins
top_9_origins = df_origin_grouped.nlargest(9)

# Calculate the sum of the rest
rest_sum = df_origin_grouped.sum() - top_9_origins.sum()

# Create a new Series for the top 9 and the rest
top_10 = top_9_origins.append(pd.Series({'Other': rest_sum}))

# Plot the top 10 countries
plt.figure(figsize=(10, 6))
top_10.plot(kind='bar')
plt.title('Top 10 Countries by Total Refugees')
plt.xlabel('Country')
plt.ylabel('Total Refugees')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('top_10_countries_refugees.png')
plt.show()

#########################

df_asylum_seekers = df[['Year', 'Asylum.seekers..pending.cases.']]

# Group by year and sum the asylum seekers pending cases
df_asylum_seekers_grouped = df_asylum_seekers.groupby('Year')['Asylum.seekers..pending.cases.'].sum()

# Example 3: Line Plot - Asylum Seekers Pending Cases Over Time
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

# Get the top 10 years with the most refugees
top_10_years = df_yearly_population.nlargest(10)

# Example 4: Bar Plot - Top 10 Years by Total Refugees
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

# Sort the values and get the top 9 countries
top_9_asylum_countries = df_asylum.nlargest(9)

# Calculate the sum of the rest
rest_sum_asylum = df_asylum.sum() - top_9_asylum_countries.sum()

# Create a new Series for the top 9 and the rest
top_10_asylum = top_9_asylum_countries.append(pd.Series({'Other': rest_sum_asylum}))

# Example 5: Bar Plot - Top 10 Countries by Total Refugees (including 'Other' category)
plt.figure(figsize=(12, 8))
top_10_asylum.plot(kind='bar')
plt.title('Top 10 Countries by Total Refugees (Including Others)')
plt.xlabel('Country/Territory of Asylum Residence')
plt.ylabel('Total Refugees')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('top_10_countries_asylum.png')
plt.show()