import zipfile
import os

def install(zip_path):
    folder = zip_path.replace(".zip", "")

    os.makedirs(folder, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(folder)

    print("[pkg] installed", zip_path)
