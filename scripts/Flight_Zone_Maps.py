import os
import requests
import math

# ✅ Replace with your actual Google Maps API key
GOOGLE_API_KEY = "AIzaSyA6tU0GBtKfj9RbpTzLBzqWX8vgr0CCMBY"  # 🔴 Replace this with your API key!

# ✅ Define the flight zone (Tallinn Example)
top_left_lat, top_left_long = 59.438, 24.730  # Modify for your area
bottom_right_lat, bottom_right_long = 59.429, 24.750  # Modify for your area
zoom = 18  # Change for resolution

# ✅ Define tile size in degrees (based on zoom level)
def get_lat_lon_step(zoom):
    """Calculate the step size for latitude & longitude per tile at a given zoom level."""
    EARTH_CIRCUMFERENCE = 40075016.686  # in meters
    TILE_SIZE_PIXELS = 640  # Google Maps API max size
    METERS_PER_PIXEL = EARTH_CIRCUMFERENCE / (256 * (2 ** zoom))
    TILE_SIZE_DEGREES = METERS_PER_PIXEL * TILE_SIZE_PIXELS / 111320  # Approx. degrees per tile

    return TILE_SIZE_DEGREES

# ✅ Calculate correct step size
lat_step = get_lat_lon_step(zoom)
lon_step = lat_step / math.cos(math.radians(top_left_lat))  # Adjust longitude step for latitude

# ✅ Output folder
output_folder = os.path.join(os.getcwd(), "google_flight_zone")
os.makedirs(output_folder, exist_ok=True)

# ✅ Download multiple tiles
lat = top_left_lat
while lat > bottom_right_lat:  # Move downward row by row
    lon = top_left_long
    while lon < bottom_right_long:  # Move right column by column
        # ✅ Construct Google Maps API URL for this tile
        tile_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=640x640&maptype=satellite&key={GOOGLE_API_KEY}"

        output_file = os.path.join(output_folder, f"{lat:.6f}_{lon:.6f}_{zoom}.jpg")

        print(f"🚀 Downloading tile at lat={lat}, lon={lon}...")
        response = requests.get(tile_url, stream=True)

        if response.status_code == 200:
            with open(output_file, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ Tile saved: {output_file}")
        else:
            print(f"❌ ERROR: Failed to download tile at lat={lat}, lon={lon} - HTTP {response.status_code}")

        lon += lon_step  # Move right to next longitude
    
    lat -= lat_step  # Move down to next latitude

print("✅ Flight Zone Download Complete!")
