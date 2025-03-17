import os
import requests

# ✅ Set up Google Maps API Key (replace with your actual key)
GOOGLE_API_KEY = "AIzaSyA6tU0GBtKfj9RbpTzLBzqWX8vgr0CCMBY"  # place this with your key!

# ✅ Set correct tile coordinates for Tallinn City Center
lat, lon, zoom = 59.434081, 24.743662, 15  # Modify as needed

# ✅ Google Maps Satellite URL
TMS_URL = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=640x640&maptype=satellite&key={GOOGLE_API_KEY}"

# ✅ Set output folder and filename
output_folder = os.path.join(os.getcwd(), "google_satellite_images")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, f"tallinn_{zoom}.jpg")

# ✅ Download the image
print(f"🚀 Downloading Google Maps satellite image for {lat}, {lon}, zoom {zoom}...")
response = requests.get(TMS_URL, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print(f"✅ Google Maps image downloaded! Check: {output_file}")
else:
    print(f"❌ ERROR: Failed to download image - HTTP {response.status_code}")
