import pandas as pd
'''Tell me you're name and i will give you a list of names that begins with you're name characters'''

df= pd.read_csv('nato_phonetic_alphabet.csv')

user_name= input("What is you're name?").strip()

df_dict= {row['letter']:row['code'] for index,row in df.iterrows()}

results=[df_dict[ch] for ch in user_name.upper()]

print(results)