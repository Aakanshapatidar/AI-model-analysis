import pandas as pd

# Load the CSV
df = pd.read_csv("clean.csv")

# 1. Quick look at the data
print(df.head())
print(df.tail())

# 2. Check for null values
print("\nNull values per column:")
print(df.isnull().sum())

# 3. Check for duplicate rows
print("\nDuplicate rows:")
print(df[df.duplicated()])

# 4. Drop duplicates if needed
df_clean = df.drop_duplicates()

# 5. Check data types
print("\nData types:")
print(df.dtypes)

# 6. Convert numeric columns (Price, Speed, Latency) to proper types
df['Price (Blended USD/1M Tokens)'] = (
    df['Price (Blended USD/1M Tokens)']
    .str.replace('$','')
    .str.strip()
    .astype(float)
)



# Count of unique models
print("\nNumber of unique models:", df['Model'].nunique())

# Convert Intelligence Index to numeric
df['Intelligence Index'] = pd.to_numeric(df['Intelligence Index'], errors='coerce')

# Step 1: Fill NaN with group mean (where available)
df['Intelligence Index'] = df.groupby('Model')['Intelligence Index'].transform(
    lambda x: x.fillna(x.mean())
)

# Step 2: For models where *all* values are NaN, fill with global mean
global_mean = df['Intelligence Index'].mean()
df['Intelligence Index'] = df['Intelligence Index'].fillna(global_mean)

# Verify
print("Remaining nulls:", df['Intelligence Index'].isnull().sum())

def convert_to_k(value):
    value = str(value).lower().strip()
    if value.endswith("k"):
        return float(value.replace("k", ""))  # already in k
    elif value.endswith("m"):
        return float(value.replace("m", "")) * 1000  # convert millions to thousands
    else:
        return pd.to_numeric(value, errors="coerce")  # fallback

# Apply conversion
df["Context Window"] = df["Context Window"].apply(convert_to_k)

# Save back to CSV
df.to_csv("cleaned_output_final.csv", index=False)


# Save cleaned data to new CSV
df.to_csv("cleaned_output1.csv", index=False)