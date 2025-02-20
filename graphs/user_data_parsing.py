import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint

current_file_path = Path(__file__)
current_folder_path = current_file_path.parent
df = pd.read_csv(current_file_path.parent.resolve() / '..'/ "data" / 'raw_data' / "new_amplitude_export_2025_chunk_1000000_1100000.csv")


user_data = df[['city', 'amplitude_id', 'country', 'device_family', 'os_version', 'platform', 'region']]
user_data = user_data.groupby('amplitude_id', as_index=False).agg({
    'city': 'first',
    'country': 'first',
    'device_family': 'first',
    'os_version': 'first',
    'platform': 'first',
    'region': 'first'
})

if __name__ == '__main__':
    pprint(user_data.head())


    def userUniqueItem(columnName):
        uniqueItems = []

        for i in range(0,len(user_data)):
            if user_data[columnName][i] not in uniqueItems:
                uniqueItems.append(user_data[columnName][i])
        print(uniqueItems)

    def userItems(columnName):
        items = []
        for i in range(0,len(user_data)):
            items.append(user_data[columnName][i])
        print(items)


    #userUniqueItem('country')
    userItems('country')