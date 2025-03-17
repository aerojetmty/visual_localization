import os
import math
import requests

# Google Maps API Key 
GOOGLE_API_KEY = "API KEY HERE!!!"  

# flight zone
top_left_lat, top_left_long = 59.438, 24.730  # Modify 
bottom_right_lat, bottom_right_long = 59.429, 24.750  # Modify 
zoom = 18  # Change for resolution
tile_size = 640  # Google Static Maps max 640x640

# Convert Latitude/Longitude to steps
def lat_lon_to_steps(lat1, lon1, lat2, lon2, step_size):
    """Generate lat/lon grid points within the flight zone."""
    lat_steps = int(abs(lat1 - lat2) / step_size) + 1
    lon_steps = int(abs(lon1 - lon2) / step_size) + 1

    lat_points = [lat1 - i * step_size for i in range(lat_steps)]
    lon_points = [lon1 + i * step_size for i in range(lon_steps)]
    
    return lat_points, lon_points

# output folder
output_folder = os.path.join(os.getcwd(), "data/map")
os.makedirs(output_folder, exist_ok=True)

# latitude/longitude grid for the flight zone
lat_step = 0.0009  # Approximate step size for 640px at zoom 18
lon_step = 0.0012  # Adjusted for longitude distortion
lat_points, lon_points = lat_lon_to_steps(top_left_lat, top_left_long, bottom_right_lat, bottom_right_long, lat_step)

# Loop through all lat/lon positions
for lat in lat_points:
    for lon in lon_points:
        # Construct Static Maps API URL
        tile_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size={tile_size}x{tile_size}&maptype=satellite&key={GOOGLE_API_KEY}"

        # Output file
        output_file = os.path.join(output_folder, f"{lat:.6f}_{lon:.6f}_{zoom}.png")

        # Download tile
        print(f" Downloading tile at lat={lat}, lon={lon}, zoom={zoom}...")
        response = requests.get(tile_url, stream=True)

        if response.status_code == 200:
            with open(output_file, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f" Tile saved: {output_file}")
        else:
            print(f" ERROR: Failed to download tile at lat={lat}, lon={lon} - HTTP {response.status_code}")

print(" Flight Zone Download Complete! Tiles saved in 'data/maps/tiles/'")
