import pandas as pd
import matplotlib.pyplot as plt
import folium
import numpy as np

df = pd.read_csv("/tmp/SFPD.csv")
print(df[['Latitude', 'Longitude']].head(5))

df = df[df['Incident Category'] == 'Motor Vehicle Theft']
df['Incident Date'] = pd.to_datetime(df['Incident Date'])
df = df[df['Incident Date'] > '01/01/2021']
df_ = df.groupby(['Latitude','Longitude']).count().reset_index()
df = df_[['Latitude','Longitude','Incident Date']]
df.columns = ['Latitude','Longitude','count']
lat, long, count = df['Latitude'], df['Longitude'], df['count']

map = folium.Map(location=[37.779992, -122.413487])

for a, b, c in zip(lat, long, count):
    if np.isnan(a) or np.isnan(b):
        continue
folium.CircleMarker([a, b], radius=c / 2, weight=1, fill=False).add_to(map)

#hmm...seems must be in notebook
plt.show()

if False:
    import geopandas as gpd
    from shapely.geometry import Point, Polygon

    sfo = gpd.read_file("/Users/parrt/Downloads/SF Find Neighborhoods")


    geo = [Point(xy) for xy in zip(long,lat)]
    geo_df = gpd.GeoDataFrame(df,geometry=geo)
    print(geo_df)

    fig, ax = plt.subplots(figsize=(15,15))
    sfo.plot(ax=ax, color='#9CD1FF')
    #geo_df.plot(ax=ax, markersize=5, color='#EF5535')
    plt.show()