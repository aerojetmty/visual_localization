import os
import pandas as pd

# ✅ Correct input folder where tiles are stored
tiles_folder = "data/map"
output_csv = "data/map/map.csv"

# ✅ Generate metadata
metadata = []
for filename in os.listdir(tiles_folder):
    if filename.endswith(".png"):
        parts = filename.replace(".png", "").split("_")
        if len(parts) != 3:
            print(f"⚠️ Skipping {filename} - Filename format incorrect")
            continue  # Ignore files that don't match `lat_lon_zoom.png` format

        lat, lon, zoom = map(float, parts)  # ✅ Convert lat/lon to float
        zoom = int(zoom)  # ✅ Ensure zoom is an integer

        # ✅ Approximate tile size (adjust if needed)
        lat_step = 0.0009
        lon_step = 0.0012

        # ✅ Calculate bounding box (assumes north-downward tile layout)
        top_left_lat, top_left_lon = lat, lon
        bottom_right_lat = lat - lat_step  # Moves downward slightly
        bottom_right_lon = lon + lon_step  # Moves right slightly

        metadata.append([filename, top_left_lat, top_left_lon, bottom_right_lat, bottom_right_lon])

# ✅ Save metadata to `data/map/map.csv`
df = pd.DataFrame(metadata, columns=["Filename", "Top_left_lat", "Top_left_lon", "Bottom_right_lat", "Bottom_right_long"])
df.to_csv(output_csv, index=False)

print(f"✅ Metadata file saved: {output_csv}")
