# Structure

visual_localization/
│── data/
│   ├── map/                 # Satellite images
│   │   ├── <lat_lon>.png
│   │   ├── map.csv          # Metadata for satellite images
│   ├── query/               # Drone images for localization
│   │   ├── Drone_1.png
│   │   ├── photo_metadata.csv  # Metadata for drone images
│── scripts/
│   ├── main.py              # Main script to run the pipeline
│── src/
│   ├── svl/
│   │   ├── localization/
│   │   │   ├── pipeline.py  # Main localization pipeline
│   │   │   ├── map_reader.py  # Reads satellite images
│   │   │   ├── drone_streamer.py # Reads drone images
│   │   ├── models/
│   │   │   ├── superpoint.py  # Feature extractor
│   │   │   ├── superglue.py   # Feature matcher
│── README.md                 # Documentation by original author
│── documentation.md            # Documentation by us

# Needed to run the script

python 3.9! on computer with python installed in VS Code.

1. pip install poetry (first time only)

2. poetry install (first time only)

3. unistall wrong torch torchvision: pip uninstall torch torchvision -y

4. install correct torch torchvision: pip install torch==1.13.0+cu116 

5. torchvision==0.14.0+cu116 -f https://download.pytorch.org/whl/torch_stable.html

6. unistall wrong numpy: pip uninstall numpy -y

7. install correct numpy: pip install numpy==1.23.5

8. poetry shell

9. git submodule update --init --recursive

10. python scripts/main.py (main script - prepare data first)



# Prepare and run data

1. poetry add Pillow (needed to run metadata_sat)

2. pip install openpyx1 /  poetry add openpyx1

3. determine flight zone in flightzone_v2.py - change coordinates

4. py flightzone_v2.py - satellite images go to /data/map

5. py generate_metadata.py - for satellite images (/data/map/map.csv)

6. place drone images to "query" folder and add the file name and GPS coordinates to the photo_metadata Excel manually (for now!)

7. python scripts/main.py 

Now the script uses ML to go through all the images and find matches.


# Bugfixes

/ ModuleNotFoundError: No module named 'pandas'
- pip install pandas
