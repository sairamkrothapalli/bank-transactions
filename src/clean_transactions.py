import pandas as pd

print("✅ Script started...")

# Read raw CSV
df = pd.read_csv('data/raw/bank_transactions.csv')
print("📥 Raw Data:")
print(df.head())

# Drop rows with nulls
df.dropna(inplace=True)
print("✅ Dropped rows with nulls")

# Clean column names
df.columns = df.columns.str.strip().str.lower()
print("✅ Cleaned column names")

# Convert 'amount' to float (if not already)
df['amount'] = df['amount'].astype(float)
print("✅ Converted amount to float")

# Save cleaned file
df.to_csv('data/processed/cleaned_transactions.csv', index=False)
print("✅ Saved cleaned data to: data/processed/cleaned_transactions.csv")

print("\n📦 Cleaned Data:")
print(df.head())