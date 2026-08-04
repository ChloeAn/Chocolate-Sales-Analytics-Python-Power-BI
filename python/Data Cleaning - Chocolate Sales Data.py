'''Standard Python data-cleaning workflow:
1. Read the data
2. Inspect the data
3. Identify data-quality problems
4. Clean the data
5. Validate the cleaned result
6. Analyse the data
7. Export the cleaned data'''

import pandas as pd
#get data
file_path = r"Z:\Projects\Chocolate Sales\Chocolate Sales (2).csv"

df = pd.read_csv(file_path)

#inspect the first 5 rows
'''Select top 5 * from table'''
print(df.head())

#inspect the last 5 rows
print(df.tail())
#print(df)

#check dataset size (3282, 6)
print(df.shape)

#or check them separately 3282 rows, 6 columns
'''select count(*) from table'''
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

#check column names
print(df.columns)
print(df.dtypes)

#update column names to make it easier to read/use
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ","_")
)
print("Column name updated as:", df.columns)

#check data types
print(df.dtypes)
df.info()

#check missing value all 0 
print(df.isna().sum())

#can replace na to unknown or 0 for amount - not required now
#df["country"] = df["country"].fillna("unknown")

#check duplicate
print(df.duplicated().sum())
dup_rows = df[df.duplicated(keep=False)]
print(dup_rows)

#keep a copy of the original data before cleaning
df_original = df.copy()

#clean text values
#remove spaces
df["country"] = df["country"].str.strip()
df["product"] = df["product"].str.strip()
df["sales_person"] = df["sales_person"].str.strip()

#can do for every columns at once to remove spaces from the beginning and end.
text_columns = df.select_dtypes(include=["object","string"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()

#Standardise capitalisation
df["country"] = df["country"].str.title()

#check inconsistent categories
print(df["country"].unique())
print(df["country"].value_counts())

#update country name
df["country"] = df["country"].replace({
    "Usa": "USA",
    "Uk": "UK"
})

print(df["country"].value_counts())

#convert dates
print(df["date"].dtype)

#df["date"] = pd.to_datetime(df["date"])
'''
df["date"] = pd.to_datetime(df["date"],errors="coerce")
invalid_dates = df[df["date"].isna()]
print(invalid_dates)
'''
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

invalid_dates = df[df["date"].isna()]
print("\nInvalid dates:", invalid_dates.shape)

print(df["date"])

#df["year"] = df["date"].dt.year
#df["month"] = df["date"].dt.month
#df["month_name"] = df["date"].dt.month_name()
'''
df["amount"] = pd.to_numeric(
    df["amount"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip(),
    errors="coerce"
)
'''
df["boxes_shipped"] = pd.to_numeric(
    df["boxes_shipped"],
    errors="coerce"
)

#print(df.head())
#df.info()


#print(df["product"].value_counts())
#print(df["sales_person"].value_counts())

#print("\nCountries:",df["country"].value_counts(dropna=False))
#print("\nProducts:",df["product"].value_counts(dropna=False))

#check invalid values for amount and boxes_shipped
invalid_amount = df[df["amount"]<0]
invalid_boxes = df[df["boxes_shipped"]<0]
print("Invalid amounts:", invalid_amount.shape[0])
print("Invalid boxes shipped:", invalid_boxes.shape[0])

print("\nMissing values after cleaning:\n", df.isna().sum())
print("\nDuplicate rows after cleaning:", df.duplicated().sum())
print("\nData types after cleaning:\n", df.dtypes)
print("\nData types after cleaning:\n", df.shape)

#export cleaned data to a new CSV file
output_path = r"Z:\Projects\Chocolate Sales\Chocolate Sales Cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned file saved successfully.")
