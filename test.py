import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

current_file_path = Path(__file__)
current_folder_path = current_file_path.parent
df = pd.read_csv(current_file_path.parent.resolve() / "data" / 'raw_data' / "new_amplitude_export_2025_chunk_1000000_1100000.csv")

#print(df.head())

print(type(df['event_type'][0]))

list_of_words = []
for i in range(0, 100000):
    list_of_words.append(df['city'][i])

from pprint import pprint
from statistics import mode
pprint(mode(list_of_words))
#print((df['event_type'][0:100]))


from collections import Counter
counts = Counter(list_of_words)

# Find the top 5 most common strings
print(counts.most_common(5))