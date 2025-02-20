from user_data_parsing import user_data
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from collections import Counter
import os
import matplotlib.colors as mcolors

# Step 1: Get user country data
countries = user_data['country']
print("User countries:", countries)

# Step 2: Count occurrences of each country
country_counts = Counter(countries)
print("Country counts:", country_counts)

# Step 3: Load the world shapefile
script_dir = os.path.dirname(__file__)
shapefile_path = os.path.join(script_dir, "ne_110m_admin_0_countries", "ne_110m_admin_0_countries.shp")
world = gpd.read_file(shapefile_path)

# Step 4: Print available country names for debugging
print("World country names:", world["NAME"].unique())

# Step 5: Handle naming mismatches
name_mapping = {
    "United States": "United States of America",
}

# Standardize country names in user data
standardized_counts = Counter({name_mapping.get(k, k): v for k, v in country_counts.items()})

# Step 6: Map counts to the world map
world["count"] = world["NAME"].map(standardized_counts).fillna(0)

# Step 7: Plot the world map with shading based on frequency
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
norm = mcolors.LogNorm(vmin=1, vmax=world["count"].max() + 1)
world.plot(column="count", cmap="Blues", linewidth=0.8, edgecolor="black", norm = norm, legend=True, ax=ax)

# Step 8: Add title and show the plot
ax.set_title("Country Frequency Map", fontsize=14)
plt.show()

