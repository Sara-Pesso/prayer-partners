import toml
import os
os.chdir(r"E:\prayer-partners")

def update_toml_entries(field, key, new_value):
    config_info = toml.load('config.toml')
    config_info[field][key] = new_value
    with open('config.toml', "w") as f:
        toml.dump(config_info, f)

    return []

# update_toml_entries('authorized-user', 'username', 'pessognellisa20@gmail.com')