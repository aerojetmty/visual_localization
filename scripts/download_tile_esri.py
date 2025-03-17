import os
import requests

# Define coordinates
x, y, zoom = 93985, 46927, 16  # Modify

# Esri World Imagery 
TMS_URL = f"https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{zoom}/{y}/{x}"

# Headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Referer": "https://www.arcgis.com/",
}

# Output
output_folder = os.path.join(os.getcwd(), "satellite_images")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, f"{x}_{y}_{zoom}.jpg")

# Download tile
print("Downloading satellite image...")
response = requests.get(TMS_URL, headers=HEADERS, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print(f"Image downloaded! Check: {output_file}")
else:
    print(f"ERROR: Failed to download image - HTTP {response.status_code}")
