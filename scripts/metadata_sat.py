from PIL import Image
from PIL.ExifTags import TAGS

# Load image
image_path = "satellite_images/36815_18771_16.jpg"  # modify filename
image = Image.open(image_path)

# Extract metadata
exif_data = image._getexif()

if exif_data:
    print("Image Metadata:")
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
else:
    print("No EXIF metadata found in the image.")


# poetry add Pillow - needed to run the script
