import pandas as pd

phys_cycles = pd.read_csv('raw/physiological_cycles.csv')
workouts = pd.read_csv('raw/workouts.csv')
sleep = pd.read_csv('raw/sleeps.csv')

# Convert date fields to datetime for the physiological cycles dataset and handle errors by coercing them to NaT (Not a Time).
phys_cycles['Cycle start time'] = pd.to_datetime(phys_cycles['Cycle start time'], errors='coerce')
phys_cycles['Cycle end time'] = pd.to_datetime(phys_cycles['Cycle end time'], errors='coerce')
phys_cycles['Sleep onset'] = pd.to_datetime(phys_cycles['Sleep onset'], errors='coerce')
phys_cycles['Wake onset'] = pd.to_datetime(phys_cycles['Wake onset'], errors='coerce')

# Convert date fields to datetime for the workouts dataset and handle errors by coercing them to NaT (Not a Time).
workouts['Cycle start time'] = pd.to_datetime(workouts['Cycle start time'], errors='coerce')
workouts['Cycle end time'] = pd.to_datetime(workouts['Cycle end time'], errors='coerce')
workouts['Workout start time'] = pd.to_datetime(workouts['Workout start time'], errors='coerce')
workouts['Workout end time'] = pd.to_datetime(workouts['Workout end time'], errors='coerce')

# Convert date fields to datetime for the sleep dataset and handle errors by coercing them to NaT (Not a Time).
sleep['Cycle start time'] = pd.to_datetime(sleep['Cycle start time'], errors='coerce')
sleep['Cycle end time'] = pd.to_datetime(sleep['Cycle end time'], errors='coerce')
sleep['Sleep onset'] = pd.to_datetime(sleep['Sleep onset'], errors='coerce')
sleep['Wake onset'] = pd.to_datetime(sleep['Wake onset'], errors='coerce')

# Identify missing values in the datasets.
print(phys_cycles.isnull().sum())
print(workouts.isnull().sum())
print(sleep.isnull().sum())

# Remove columns with a large quantity of missing values (Skin temp: 51%, Blood oxygen: 51%)
# and columns that are not needed for analysis from the physiological cycles dataset.
phys_cycles = phys_cycles.drop(columns=['Skin temp (celsius)', 'Blood oxygen %', 'Cycle timezone'])

# We have three columns with a large quantity of missing values in the workouts dataset:
# (Distance (meters): 81%, Altitude gain (meters): 81%, Altitude change (meters): 81%).
# We keep these columns for now, because they are of interest when analyzing GPS-recorded workouts.
# We have one column that is not needed for analysis, which is 'Cycle timezone'.
workouts = workouts.drop(columns=['Cycle timezone'])

# We have one column in the sleep dataset that is not needed for analysis, which is 'Cycle timezone'.
sleep = sleep.drop(columns=['Cycle timezone'])

# The rest of the columns have only 0 or 1 missing values (and one with 4) in the physiological cycles dataset, so we can drop those rows.
phys_cycles = phys_cycles.dropna()
phys_cycles = phys_cycles.reset_index(drop=True)

# We will also remove rows with missing values in the remaining columns in the workouts dataset.
workouts = workouts[workouts['Cycle end time'].notnull()]
workouts = workouts.reset_index(drop=True)

# We will also remove rows with missing values in the sleep dataset since there are only a few.
sleep = sleep.dropna()
sleep = sleep.reset_index(drop=True)

# Save the cleaned datasets to new CSV files
phys_cycles.to_csv('cleaned_data/cleaned_physiological_cycles.csv', index=False)
workouts.to_csv('cleaned_data/cleaned_workouts.csv', index=False)
sleep.to_csv('cleaned_data/cleaned_sleeps.csv', index=False)