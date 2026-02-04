import pandas as pd

def get_directory(file_name):
    df = pd.read_excel(file_name)
    df['full_name'] = df['Last name']+"-"+df["First name"]

    #List of names
    names = df["full_name"].tolist()

    #Convert to dictionary
    name_to_email = df.set_index("full_name").T.to_dict('list')
    return names, name_to_email
