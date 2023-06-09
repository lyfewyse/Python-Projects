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

# Print random 20 rows of data
random_sample = merged_df.sample(n=20, random_state=30)
print(random_sample)