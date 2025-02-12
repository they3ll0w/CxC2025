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




from collections import Counter
counts = Counter(list_of_words)

    # Find the top 5 most common strings
    #print(counts.most_common(5))

def mapUsers():

    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from collections import Counter
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    print(list_of_words)

    # Count the frequency of each city
    city_counts = Counter(list_of_words)

    # Predefined coordinates for cities
    city_coords = {
        'Mumbai': (19.0760, 72.8777),
        'Nashville': (36.1627, -86.7816),
        'Navarre': (30.4010, -86.8636),
        'Spring Hill': (35.7512, -86.9300),
        'Aurora': (39.7294, -104.8319),
        'Chicago': (41.8781, -87.6298),
        'Columbus': (39.9612, -82.9988),
        'Simpsonville': (34.7371, -82.2543),
        'Birmingham': (33.5186, -86.8104),
        'Alexandria': (38.8048, -77.0469),
        'New York': (40.7128, -74.0060),
        'Concord': (43.2081, -71.5376),
        'Washington': (38.9072, -77.0369),
        'Orlando': (28.5383, -81.3792),
        'St Louis': (38.6270, -90.1994),
        'Covington': (39.0837, -84.5086),
        'Houston': (29.7604, -95.3698),
        'Parma': (41.4048, -81.7229),
        'Easley': (34.8290, -82.6015),
        'Marietta': (33.9526, -84.5499),
        'McKinney': (33.1972, -96.6398),
        'Knoxville': (35.9606, -83.9207),
        'Schaumburg': (42.0334, -88.0834),
        'Ashburn': (39.0438, -77.4874),
        'Bensenville': (41.9550, -87.9401),
        'Tomball': (30.0972, -95.6161),
        'Greenville': (34.8526, -82.3940),
        'Toronto': (43.6510, -79.3470),
        'Kansas City': (39.0997, -94.5786),
        'Whittier': (33.9792, -118.0328),
        'Darby': (39.9184, -75.2580),
        'Myrtle Beach': (33.6891, -78.8867),
        'Saint Augustine': (29.9012, -81.3124),
        'Atlanta': (33.7490, -84.3880),
        'Mount Prospect': (42.0664, -87.9373),
        'Tampa': (27.9506, -82.4572),
        'Burlington': (44.4759, -73.2121),
        'Portland': (45.5152, -122.6784),
        'Huntsville': (34.7304, -86.5861),
        'Little Elm': (33.1626, -96.9375),
        'Carlsbad': (33.1581, -117.3506),
        'San Francisco': (37.7749, -122.4194),
        'South Bend': (41.6764, -86.2520),
        'Stamford': (41.0534, -73.5387),
        'Cumming': (34.2073, -84.1402),
        'Los Angeles': (34.0522, -118.2437),
        'McCalla': (33.3207, -87.0042),
        'Fort Worth': (32.7555, -97.3308),
        'Detroit': (42.3314, -83.0458),
        'Suwanee': (34.0515, -84.0713),
        'Sunnyvale': (37.3688, -122.0363),
        'San Tan Valley': (33.1706, -111.5722),
        'Forney': (32.7482, -96.4719),
        'South San Francisco': (37.6547, -122.4077),
        'Springfield': (37.2089, -93.2923),
        'Brooklyn': (40.6782, -73.9442),
        'Caldwell': (40.8395, -74.2765),
        'Howell': (40.1645, -74.2087),
        'Trumbull': (41.2420, -73.2007),
        'Arlington': (32.7357, -97.1081),
        'Oakville': (43.4675, -79.6877),
        'Dallas': (32.7767, -96.7970),
        'Granger': (41.7539, -86.1439),
        'Renton': (47.4829, -122.2171),
        'Yakima': (46.6021, -120.5059),
        'Albany': (42.6526, -73.7562),
        'Rocky Mount': (35.9382, -77.7905),
        'Lake Oswego': (45.4207, -122.6706),
        'Alajuela': (10.0153, -84.2147),
        'Spring': (30.0799, -95.4172),
        'Powder Springs': (33.8595, -84.6838),
        'Oak Park': (41.8850, -87.7845),
        'Rockford': (42.2711, -89.0937),
        'Chatsworth': (34.2506, -118.6148),
        'Ankeny': (41.7310, -93.6001),
        'Des Moines': (41.5868, -93.6250),
        'Columbia': (34.0007, -81.0348),
        'Hoboken': (40.7433, -74.0324),
        'London': (51.5074, -0.1278),
        'Pomona': (34.0551, -117.7490),
        'Earlham': (41.4950, -94.1255),
        'Urbandale': (41.6267, -93.7122),
        'Phoenix': (33.4484, -112.0740),
        'Waukee': (41.6119, -93.8858),
        'Cleveland': (41.4993, -81.6944),
        'Seattle': (47.6062, -122.3321),
        'Jamaica Plain': (42.3097, -71.1151),
        'Jackson': (32.2988, -90.1848),
        'Rolesville': (35.9232, -78.4642),
        'Wałbrzych': (50.7840, 16.2843),
        'Wroclaw': (51.1079, 17.0385),
        'Miami': (25.7617, -80.1918),
        'Indianapolis': (39.7684, -86.1581),
        'Mississauga': (43.5890, -79.6441),
        'Gloversville': (43.0526, -74.3437),
        'Monroe': (32.5093, -92.1193),
        'Rochester': (43.1566, -77.6088),
        'Buford': (34.1207, -84.0044),
        'City of Westminster': (51.4975, -0.1357),
        'Ada': (34.7745, -96.6783),
        'Charlotte': (35.2271, -80.8431),
        'Frisco': (33.1507, -96.8236),
        'Madison': (43.0731, -89.4012),
        'Kenner': (29.9941, -90.2417),
        'Bridgeport': (41.1792, -73.1894),
        'Macon': (32.8407, -83.6324),
        'Waterloo': (42.4928, -92.3426),
        'Fort Lauderdale': (26.1224, -80.1373),
        'Paradise Valley': (33.5312, -111.9426),
        'Sudbury': (46.4917, -81.0069),
        'Scarborough': (43.7764, -79.2318),
        'Sandy': (40.5648, -111.8380),
        'Orange City': (28.9489, -81.2987),
        'Boydton': (36.6671, -78.3878),
        'Parrish': (27.5300, -82.4245),
        'Fort Lee': (40.8509, -73.9701),
        'Jacksonville': (30.3322, -81.6557),
        'Greensboro': (36.0726, -79.7920),
        'Wethersfield': (41.7140, -72.6526),
        'Anaheim': (33.8366, -117.9143),
        'Riverview': (27.8661, -82.3265),
        'Puyallup': (47.1854, -122.2929),
        'Altamonte Springs': (28.6611, -81.3656),
        'Longwood': (28.7031, -81.3384),
        'Sarasota': (27.3364, -82.5307),
        'Naples': (26.1420, -81.7948),
        'St. Petersburg': (27.7676, -82.6403),
        'Albion': (42.2431, -84.7533),
        'Braintree': (42.2223, -71.0028),
        'Zabrze': (50.3249, 18.7850),
        'Kłodzko': (50.4349, 16.6610),
        'Milton': (43.5168, -79.8829),
        'Franklin Square': (40.7007, -73.6751),
        'Alpharetta': (34.0754, -84.2941),
        'Olathe': (38.8814, -94.8191),
        'Chandler': (33.3062, -111.8413),
        'Boca Raton': (26.3683, -80.1289),
        'Kitchener': (43.4516, -80.4925),
        'Miguel Hidalgo': (19.4344, -99.2001),
        'Corpus Christi': (27.8006, -97.3964),
        'Newnan': (33.3807, -84.7997),
        'Milford': (41.2307, -73.0640),
        'Miramar': (25.9873, -80.2323),
        'Davie': (26.0765, -80.2521),
        'Dubuque': (42.5006, -90.6646),
        'Moca': (18.9221, -67.0597),
        'Boardman': (41.0242, -80.6629),
        'San Jose': (37.3382, -121.8863),
        'Elkridge': (39.2126, -76.7261),
        'Greenfield': (39.7687, -86.7714),
        'Powell': (40.1576, -83.0752),
        'Richmond': (37.5407, -77.4360),
        'Thomaston': (41.6745, -73.0734),
        'Sammamish': (47.6163, -122.0356),
        'Gilbert': (33.3528, -111.7890),
        'Scottsdale': (33.4942, -111.9261),
        'Union City': (40.6976, -74.0570),
        'Putnam Valley': (41.3360, -73.8487),
        'Boston': (42.3601, -71.0589),
        'Newark': (40.7357, -74.1724),
        'Larchmont': (40.9279, -73.7515),
        'Loveland': (40.3978, -105.0749),
        'Flanders': (50.8503, 4.3517),
        'Middletown': (41.4459, -74.4229),
        'Port Orchard': (47.5407, -122.6361),
        'Stockton': (37.9577, -121.2908),
        'Warsaw': (52.2298, 21.0122),
    }

    # Create a map
    fig, ax = plt.subplots(
        figsize=(10, 6),
        subplot_kw={"projection": ccrs.PlateCarree()}
    )

    # Set the extent of the map delimitation
    ax.set_extent([-130, -60, 20, 55])
    #ax.set_global()

    # Add map features
    ax.add_feature(cfeature.LAND, edgecolor="black")
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=":")

    # Plot each city with a circle size proportional to its frequency
    for city, (lat, lon) in city_coords.items():
        frequency = city_counts[city]
        ax.scatter(
            lon, lat,  # Longitude and latitude
            s=frequency * 20,  # Circle size (scaled by frequency)
            color="red",  # Circle color
            alpha=0.6,  # Transparency
            edgecolor="black",  # Circle border
            transform=ccrs.PlateCarree(),
        )

    # Add title
    ax.set_title("Federato Website Usage", fontsize=16)

    # Remove legend
    # ax.legend()  # Commented out to remove the legend

    # Show the map
    plt.show()

if __name__ == '__main__':
    mapUsers()

#POUR ROBERT
def cityRadiusSize(list_of_cities): #where list_of_words is the list of unique cities
    base_radius = 5  # Minimum size
    scaling_factor = 3  # Adjust size growth

    
    city_radius = {city: base_radius + (count * scaling_factor) for city, count in Counter(list_of_cities).items()}

    #
    print(city_radius)

cityRadiusSize(list_of_words)