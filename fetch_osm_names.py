import osmnx as ox
import geopandas as gpd
import json

def fetch_osm_names(city):
    print(f"Fetching OSM names for {city}...")
    boundary = gpd.read_file(f'/home/levente/projects/gator/2026/geoai_paddeaux/{city}_4326.geojson')
    polygon = boundary.geometry.iloc[0]
    
    tags = {'amenity': ['restaurant', 'cafe', 'fast_food', 'bar', 'pub']}
    try:
        pois = ox.features_from_polygon(polygon, tags)
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return
        
    names = set()
    if 'name' in pois.columns:
        for name in pois['name'].dropna():
            names.add(str(name).lower().strip())
            
    with open(f'/home/levente/projects/gator/2026/geoai_paddeaux/{city}_osm_names.json', 'w') as f:
        json.dump(list(names), f)
    print(f"Saved {len(names)} unique names for {city}.")

fetch_osm_names('london')
fetch_osm_names('berlin')
