import cv2
import numpy as np
from lib.lah_hapus import hapus_metadata, tampilkan_metadata
from lib.lah_hitam import hitamkan_kulit

input_image_path = './assets/images.jpeg'
output_image_path = './assets/result_image.jpg'

print("Metadata Sebelum Penghapusan:")
tampilkan_metadata(input_image_path)

hitamkan_kulit(input_image_path, output_image_path)

hapus_metadata(output_image_path)

print("\nMetadata Setelah Penghapusan:")
tampilkan_metadata(output_image_path)
