import os
import requests

# Tile coordinates and zoom level
x, y, zoom = 36815, 18771, 16

# OpenStreetMap Tile URL
TMS_URL = f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png"

# Headers to mimic a real browser request (fixes 403)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Referer": "https://www.openstreetmap.org/",
}

# output folder and filename
output_folder = os.path.join(os.getcwd(), "satellite_images")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, f"{x}_{y}_{zoom}.png")

# downloading the tile
print(" Downloading tile...")
response = requests.get(TMS_URL, headers=HEADERS, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print(f"Tile downloaded successfully! Check: {output_file}")
else:
    print(f"ERROR: Failed to download tile - HTTP {response.status_code}")
