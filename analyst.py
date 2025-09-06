import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading
df = pd.read_csv('datafm20.csv')
print('Data loaded successfully.')

# 2. Data Exploration
print('\nColumn names:')
print(df.columns.tolist())
print('\nData types:')
print(df.dtypes)
print('\nFirst 5 rows:')
print(df.head())

# 3. Data Cleaning
print('\nMissing values per column:')
print(df.isnull().sum())
print('\nDuplicate rows:', df.duplicated().sum())

# 4. Summary Statistics
print('\nSummary statistics for numeric columns:')
print(df.describe())

# 5. Visualization
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
	plt.figure(figsize=(8, 4))
	sns.histplot(df[col].dropna(), kde=True)
	plt.title(f'Distribution of {col}')
	plt.xlabel(col)
	plt.ylabel('Frequency')
	plt.tight_layout()
	plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# 6. Insights
# Top 10 players by rating (CA)
if 'CA' in df.columns:
	top10 = df.sort_values(by='CA', ascending=False).head(10)
	print('\nTop 10 Players by CA:')
	print(top10[['Name','Position','Club','CA']])

# Average CA by Division
if 'CA' in df.columns and 'Division' in df.columns:
	trend = df.groupby('Division')['CA'].mean().sort_values(ascending=False)
	print('\nAverage Current Ability by Division:')
	print(trend)
	plt.figure(figsize=(10,6))
	sns.barplot(x=trend.index, y=trend.values)
	plt.xticks(rotation=45)
	plt.title('Average Current Ability by Division')
	plt.xlabel('Division')
	plt.ylabel('Mean CA')
	plt.tight_layout()
	plt.show()
