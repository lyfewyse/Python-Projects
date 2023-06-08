import pandas as pd

# set number of columns to display
df = pd.set_option('display.max_columns', 8)

# Read CSV files
general = pd.read_csv("HyperSkill/Hospital Data Analysis/test/general.csv")
prenatal = pd.read_csv("HyperSkill/Hospital Data Analysis/test/prenatal.csv")
sports = pd.read_csv("HyperSkill/Hospital Data Analysis/test/sports.csv")

# rename columns
# Change column names in prenatal DataFrame
prenatal = prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})

# Change column names in sports DataFrame
sports = sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

# Merge Data Frames into one
merged_df = pd.concat([general, prenatal, sports], ignore_index=True)

# Delete the Unnamed: 0 column

merged_df = merged_df.drop(columns=['Unnamed: 0'], axis=1)

# Delete the empty rows

merged_df = merged_df.dropna(how='all')

# Correct gender column values

merged_df['gender'] = merged_df['gender'].replace({'female': 'f', 'male': 'm', 'man': 'm', 'woman': 'f'})

# Replace NaN values in the gender column of prenatal hospital with 'f'

merged_df.loc[merged_df['hospital'] == 'prenatal', 'gender'] = \
merged_df.loc[merged_df['hospital'] == 'prenatal', 'gender'].fillna('f')

# Replace NaN values in specific columns with zeros

columns_to_fill = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
merged_df[columns_to_fill] = merged_df[columns_to_fill].fillna(0)

# Print shape of the resulting DataFrame
 # print("Data shape:", merged_df.shape)

# Print random 20 rows of data
# random_sample = merged_df.sample(n=20, random_state=30)
# print(random_sample)

# Which hospital has the highest number of patients?
hospital_patient_counts = merged_df['hospital'].value_counts()
hospital_with_highest_patients = hospital_patient_counts.idxmax()

# What share of the patients in the general hospital suffers from stomach-related issues?
general_stomach_share = round((merged_df.loc[(merged_df['hospital'] == 'general') & (merged_df['diagnosis'] == 'stomach')].shape[0] / merged_df.loc[merged_df['hospital'] == 'general'].shape[0]), 3)

# What share of the patients in the sports hospital suffers from dislocation-related issues?
sports_dislocation_share = round((merged_df.loc[(merged_df['hospital'] == 'sports') & (merged_df['diagnosis'] == 'dislocation')].shape[0] / merged_df.loc[merged_df['hospital'] == 'sports'].shape[0]), 3)

# What is the difference in the median ages of the patients in the general and sports hospitals?
general_median_age = merged_df.loc[merged_df['hospital'] == 'general', 'age'].median()
sports_median_age = merged_df.loc[merged_df['hospital'] == 'sports', 'age'].median()
age_median_difference = round(general_median_age - sports_median_age, 1)

# After data processing at the previous stages, find the hospital with the most blood tests taken
blood_tests_by_hospital = pd.pivot_table(merged_df, index='hospital', columns='blood_test', values='age', aggfunc='count')
blood_tests_by_hospital = blood_tests_by_hospital.fillna(0)
hospital_with_most_blood_tests = blood_tests_by_hospital['t'].idxmax()
num_blood_tests_taken = blood_tests_by_hospital.loc[hospital_with_most_blood_tests, 't']

# Output the answers

# Which hospital has the highest number of patients?
print(f"The answer to the 1st question is {hospital_with_highest_patients}")

# What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
print(f"The answer to the 2nd question is {general_stomach_share}")

# What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
print(f"The answer to the 3rd question is {sports_dislocation_share}")

# What is the difference in the median ages of the patients in the general and sports hospitals?
print(f"The answer to the 4th question is {age_median_difference}")

# After data processing at the previous stages, the blood_test column has three values: t = a blood test was taken,
# f = a blood test wasn't taken, and 0 = there is no information. In which hospital the blood test was taken the most
# often (there is the biggest number of t in the blood_test column among all the hospitals)?
# How many blood tests were taken?
print(f"The answer to the 5th question is {hospital_with_most_blood_tests}, {num_blood_tests_taken}")
