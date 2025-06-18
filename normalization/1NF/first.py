import pandas as pd

# Read in the cleaned data
clean_phys = pd.read_csv('cleaned_data/cleaned_physiological_cycles.csv', parse_dates=['Cycle start time', 'Cycle end time', 'Sleep onset', 'Wake onset'])
clean_work = pd.read_csv('cleaned_data/cleaned_workouts.csv', parse_dates=['Cycle start time', 'Cycle end time', 'Workout start time', 'Workout end time'])
clean_sleep = pd.read_csv('cleaned_data/cleaned_sleeps.csv', parse_dates=['Cycle start time', 'Cycle end time', 'Sleep onset', 'Wake onset'])

# A list of common delimiters to check for non-atomic values
delimiters = [',', ';', '|', '/', '[', ']']

# Add all datasets to a dictionary for easier iteration
datasets = {
    "physiological_cycles": clean_phys,
    "workouts": clean_work,
    "sleeps": clean_sleep
}

# Run atomicity analysis
for name, df in datasets.items():
    print(f"\nAnalyzing '{name}'...")
    for col in df.select_dtypes(include='object').columns:
        for delimiter in delimiters:
            if df[col].astype(str).str.contains(delimiter, regex=False).any():
                print(f"Non-atomic values found in column: '{col}' (delimiter: '{delimiter}')")

# Check for uniqueness of rows:
phys_dup = clean_phys[clean_phys.duplicated()]
workouts_dup = clean_work[clean_work.duplicated()]
sleep_dup = clean_sleep[clean_sleep.duplicated()]
print(f"Number of duplicate rows: {phys_dup.shape[0]}")
print(f"Number of duplicate rows: {workouts_dup.shape[0]}")
print(f"Number of duplicate rows: {sleep_dup.shape[0]}")

# Check for mixed data types:
for name, df in datasets.items():
    print(f"\nAnalyzing dataset: {name}")

    for col in df.columns:
        unique_types = df[col].map(type).nunique()
        if unique_types > 1:
            print(f"Column '{col}' contains multiple data types.")
