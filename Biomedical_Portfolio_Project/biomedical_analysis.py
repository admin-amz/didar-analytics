import pandas as pd
import numpy as np

file_path = r"pythonApps\Biomedical_Portfolio_Project\biomedical_research_data.xlsx"

# 🔹 Load raw table-style data
df = pd.read_csv(file_path, sep='|', skiprows=2, header=0).iloc[:, 1:-1]
df.columns = ['Participant_ID', 'Age', 'Gender', 'Country', 'Disease', 'Research_Status', 'Study_Group']

# 🔹 Clean string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
df = df[df['Participant_ID'] != '--------------']

# ✅ FUTURE-PROOF DEBUG (important)
print("Rows loaded:", len(df))
print("\nSample Data Preview:")
print(df.head())

# 🔹 Data cleaning
df = df.drop_duplicates()
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df[(df["Age"] >= 0) & (df["Age"] <= 120)]

# 🔹 Filter by research status
active_df = df[df["Research_Status"] == "Active"]
completed_df = df[df["Research_Status"] == "Completed"]
terminated_df = df[df["Research_Status"] == "Terminated"]

# 🔹 Demographic statistics (NumPy)
total_participants = len(df)
average_age = np.mean(df["Age"])
median_age = np.median(df["Age"])
std_age = np.std(df["Age"])
male_count = np.sum(df["Gender"] == "Male")
female_count = np.sum(df["Gender"] == "Female")
country_count = df["Country"].nunique()
disease_count = df["Disease"].nunique()

demo_stats = pd.DataFrame({
    "Metric": [
        "Total Participants",
        "Average Age",
        "Median Age",
        "Age Std Deviation",
        "Male Count",
        "Female Count",
        "Countries Covered",
        "Diseases Studied"
    ],
    "Value": [
        total_participants,
        round(average_age, 1),
        round(median_age, 1),
        round(std_age, 1),
        male_count,
        female_count,
        country_count,
        disease_count
    ]
})

# 🔹 Write output Excel
output_file = "Processed_Biomedical_Data.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    active_df.to_excel(writer, sheet_name="Active_Studies", index=False)
    completed_df.to_excel(writer, sheet_name="Completed_Studies", index=False)
    terminated_df.to_excel(writer, sheet_name="Terminated_Studies", index=False)
    demo_stats.to_excel(writer, sheet_name="Demographic_Statistics", index=False)

print("\n✅ Biomedical data processed successfully!")
print("📁 Output file created:", output_file)

