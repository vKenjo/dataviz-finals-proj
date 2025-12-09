"""
Transform World Bank data from wide to long format
"""

import pandas as pd
import numpy as np

print("Loading data...")
df_raw = pd.read_csv("data/data.csv")
print(f"✓ Loaded {len(df_raw):,} records")

# Get year columns
year_cols = [col for col in df_raw.columns if "[YR" in col]
print(f"Found {len(year_cols)} year columns")

# Melt to long format
print("Transforming to long format...")
df_long = df_raw.melt(
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    value_vars=year_cols,
    var_name="year_col",
    value_name="value",
)

# Extract year from column name (e.g., "1990 [YR1990]" -> 1990)
df_long["year"] = df_long["year_col"].str.extract(r"(\d{4})").astype(int)
df_long = df_long.drop("year_col", axis=1)

# Replace '..' with NaN and convert to numeric
df_long["value"] = pd.to_numeric(
    df_long["value"].replace("..", np.nan), errors="coerce"
)

# Pivot to get indicators as columns
print("Pivoting to wide format with indicators as columns...")
df = df_long.pivot_table(
    index=["Country Name", "Country Code", "year"],
    columns="Series Name",
    values="value",
    aggfunc="first",
).reset_index()

# Rename columns to shorter names
df.columns.name = None
df = df.rename(
    columns={
        "Country Name": "country",
        "Country Code": "country_code",
        "Poverty headcount ratio at $3.00 a day (2021 PPP) (% of population)": "poverty_headcount",
        "School enrollment, primary (% net)": "primary_enrollment",
        "School enrollment, secondary (% gross)": "secondary_enrollment",
        "Access to electricity (% of population)": "electricity_access",
        "GDP per capita (current US$)": "gdp_per_capita",
        "Life expectancy at birth, total (years)": "life_expectancy",
        "Population, total": "population",
    }
)

# Save transformed data
output_file = "data/data_transformed.csv"
df.to_csv(output_file, index=False)

print(f"\n✓ Transformed data saved to {output_file}")
print(f"✓ Shape: {df.shape}")
print(f"✓ Years: {df['year'].min():.0f} - {df['year'].max():.0f}")
print(f"✓ Countries: {df['country'].nunique()}")
print(f"✓ Columns: {list(df.columns)}")
print("\nSample with poverty data:")
print(df[df["poverty_headcount"].notna()].head())
