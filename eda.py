# =========================================================
# CODEALPHA EDA PROJECT - NETFLIX DATASET
# =========================================================

# -------------------------------
# IMPORT LIBRARIES
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# -------------------------------
# LOAD DATASET
# -------------------------------

df = pd.read_csv("netflix_titles.csv")

# -------------------------------
# BASIC INFORMATION
# -------------------------------

print("\n FIRST 5 ROWS\n")
print(df.head())

print("\n DATASET INFO\n")
print(df.info())

print("\n DATASET SHAPE\n")
print(df.shape)

print("\n MISSING VALUES\n")
print(df.isnull().sum())

print("\n DUPLICATE VALUES\n")
print(df.duplicated().sum())

# -------------------------------
# DATA CLEANING
# -------------------------------

df.drop_duplicates(inplace=True)

df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)

df.dropna(subset=['date_added', 'duration'], inplace=True)

# -------------------------------
# DATE CONVERSION
# -------------------------------

df['date_added'] = pd.to_datetime(df['date_added'])

df['year_added'] = df['date_added'].dt.year

# -------------------------------
# DURATION CLEANING
# -------------------------------

df['duration_int'] = df['duration'].str.extract('(\d+)')

df['duration_int'] = pd.to_numeric(df['duration_int'])

# -------------------------------
# MOVIES VS TV SHOWS
# -------------------------------

plt.figure(figsize=(6,4))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")

plt.savefig("movies_vs_tvshows.png")

plt.show()

# =========================================================
# TOP 10 COUNTRIES
# =========================================================

top_country = df['country'].value_counts().head(10)

plt.figure(figsize=(12,5))

sns.barplot(x=top_country.index,
            y=top_country.values)

plt.title("Top 10 Countries with Most Netflix Content")

plt.xticks(rotation=45)

plt.savefig("top_countries.png")

plt.show()

# =========================================================
# RELEASE YEAR DISTRIBUTION
# =========================================================

plt.figure(figsize=(10,5))

sns.histplot(df['release_year'],
             bins=30,
             kde=True)

plt.title("Distribution of Release Years")

plt.savefig("release_year_distribution.png")

plt.show()

# =========================================================
# MISSING VALUES HEATMAP
# =========================================================

plt.figure(figsize=(12,6))

sns.heatmap(df.isnull(),
            cbar=False,
            yticklabels=False,
            cmap='viridis')

plt.title("Missing Values Heatmap")

plt.savefig("missing_values_heatmap.png")

plt.show()

# =========================================================
# CORRELATION HEATMAP
# =========================================================

plt.figure(figsize=(6,4))

corr = df[['release_year', 'duration_int']].corr()

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.show()

# =========================================================
# BOXPLOT
# =========================================================

plt.figure(figsize=(8,5))

sns.boxplot(x=df['release_year'])

plt.title("Boxplot of Release Years")

plt.savefig("boxplot_release_year.png")

plt.show()

# =========================================================
# FINAL INSIGHTS
# =========================================================

print("\n PROJECT INSIGHTS\n")

print("1. Netflix has more Movies than TV Shows.")
print("2. USA contributes highest Netflix content.")
print("3. Content increased rapidly after 2015.")
print("4. Some outliers exist in release years.")

print("\n EDA PROJECT COMPLETED SUCCESSFULLY")