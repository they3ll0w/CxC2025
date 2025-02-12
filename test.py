import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

current_file_path = Path(__file__)
current_folder_path = current_file_path.parent
df = pd.read_csv(current_file_path.parent.resolve() / "data" / "new_amplitude_export_2025_chunk_1000000_1100000.csv")


print(df.head())

print(type(df[0][0]))