import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

current_file_path = Path(__file__)
current_folder_path = current_file_path.parent
df = pd.read_csv(current_file_path.parent.resolve() / "data" / 'raw_data' / "new_amplitude_export_2025_chunk_1000000_1100000.csv")

#print(df.head())

user_data = df[['city', 'amplitude_id', 'country', 'device_family', 'os_version', 'platform', 'region']]
user_data = user_data.groupby('amplitude_id', as_index=False).agg({
    'city': 'first',
    'country': 'first',
    'device_family': 'first',
    'os_version': 'first',
    'platform': 'first',
    'region': 'first'
})


list_of_words = []
for i in range(0,len(user_data)):
    list_of_words.append(user_data['city'][i])

from pprint import pprint
from statistics import mode
pprint(mode(list_of_words))
#print((df['event_type'][0:100]))