import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\Summer-Olympic-medals-1976-to-2008(1).csv', encoding='latin1')


print(df.head(10))
# Step 2️⃣: Explore dataset
print("----- BASIC INFO -----")
print(df.info())
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())
print("\n----- FIRST 5 ROWS -----")
print(df.head())

# Step 3️⃣: Basic details
years = df['Year'].unique()
num_sports = df['Sport'].nunique()
num_countries = df['Country'].nunique()

print("\nYears Covered:", years)
print("Number of Sports:", num_sports)
print("Number of Countries:", num_countries)

# Step 4️⃣: Total medals by country
country_medals = df['Country'].value_counts().head(10)
print("\n----- TOP 10 COUNTRIES (TOTAL MEDALS) -----")
print(country_medals)

# Step 5️⃣: Gold medals by country
gold_medals = df[df['Medal'] == 'Gold']['Country'].value_counts().head(10)
print("\n----- TOP 10 COUNTRIES (GOLD MEDALS) -----")
print(gold_medals)

# Step 6️⃣: Medals over time
medals_by_year = df.groupby('Year')['Medal'].count()

plt.figure(figsize=(8,5))
plt.plot(medals_by_year.index, medals_by_year.values, color='orange', marker='o', linewidth=2)
plt.title('Total Medals Over the Years (1976–2008)', fontsize=13)
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.grid(True)
plt.show()

# Step 7️⃣: Top athletes
top_athletes = df['Athlete'].value_counts().head(10)
print("\n----- TOP 10 ATHLETES BY MEDALS -----")
print(top_athletes)

# Step 8️⃣: Top sports
top_sports = df['Sport'].value_counts().head(10)
print("\n----- TOP 10 SPORTS BY MEDALS -----")
print(top_sports)

# Step 9️⃣: Visualizations

# a) Total Medals by Country
country_medals.plot(kind='bar', color='skyblue', title='Top 10 Countries by Total Medals', figsize=(8,5))
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.show()

# b) Gold Medals by Country
gold_medals.plot(kind='bar', color='gold', title='Top 10 Countries by Gold Medals', figsize=(8,5))
plt.xlabel('Country')
plt.ylabel('Gold Medals')
plt.show()

# c) Top Sports
top_sports.plot(kind='barh', color='lightgreen', title='Top 10 Sports by Medal Count', figsize=(8,5))
plt.xlabel('Total Medals')
plt.ylabel('Sport')
plt.show()

print("\n✅ ANALYSIS COMPLETE — Dataset covers 9 Olympics (1976–2008).")

#Gender distribution of events and medals
gender_medal_count = df['Gender'].value_counts()

print("Medal distribution by Gender:")
print(gender_medal_count)

gender_medal_count.plot(kind='bar', color=['skyblue', 'lightcoral', 'gold'])
plt.title('Gender Distribution of Medals')
plt.xlabel('Gender')
plt.ylabel('Number of Medals')
plt.show()

gender_event_count = df[['Event', 'Gender']].drop_duplicates()['Gender'].value_counts()

print("Event distribution by Gender:")
print(gender_event_count)
gender_event_count.plot(kind='bar', color=['lightgreen', 'lightpink', 'orange'])
plt.title('Gender Distribution of Events')
plt.xlabel('Gender')
plt.ylabel('Number of Events')
plt.show()
