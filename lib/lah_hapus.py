import subprocess

def hapus_metadata(image_path):
    subprocess.run(["exiftool", "-all=", image_path])

def tampilkan_metadata(image_path):
    metadata = subprocess.check_output(["exiftool", image_path])
    print(metadata.decode())
