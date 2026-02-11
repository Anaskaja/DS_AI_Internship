import pandas as pd

usernames=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

remove_whitespaces=usernames.str.strip()
lowercase =remove_whitespaces.str.lower()
contains_a =lowercase.str.contains('a')

print(remove_whitespaces)
print(lowercase)
print(contains_a)