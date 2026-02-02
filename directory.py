import pandas as pd

file = "E:\prayer-partners\directory.xlsx"
df = pd.read_excel(file)
df['full_name'] = df['Last name']+"-"+df["First name"]

#List of names
names = df["full_name"].tolist()

#Convert to dictionary
name_to_email = df.set_index("full_name").T.to_dict('list')
