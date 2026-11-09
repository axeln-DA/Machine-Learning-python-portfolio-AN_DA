
import pandas as pd

# Create a fictional disease surveillance dataset
data = {
    "District": ["Ngoma", "Kayonza", "Kirehe", "Ngoma", "Kirehe"],
    "Age": [34, 49, 28, 41, 52],
    "Fever": [1, 1, 0, 1, 1],
    "Confirmed": [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Display the dataset
print("SURVEILLANCE DATASET")
print(df)

# Count records
print("\nTOTAL RECORDS")
print(len(df))

# Calculate confirmation percentage
confirmation_rate = df["Confirmed"].mean() * 100

print("\nCONFIRMATION RATE")
print(f"{confirmation_rate:.1f}%")

# Summarize confirmed cases by district
print("\nCONFIRMED CASES BY DISTRICT")
print(df.groupby("District")["Confirmed"].sum())
