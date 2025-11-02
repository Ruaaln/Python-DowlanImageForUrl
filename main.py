import requests
from random import randint
import os

# Scriptin olduğu qovluğun yolunu al
base_folder = os.path.dirname(os.path.abspath(__file__))

# "yuklenenler" qovluğunu base_folder içində yarat
folder = os.path.join(base_folder, "Download")
if not os.path.exists(folder):
    os.makedirs(folder)

while True:
    url = input("Enter URL: ")
    if url.lower() in ("exit", "quit"):
        break

    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(folder, f"downloaded_image_{randint(1000, 100000)}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Dowland successful: {file_path}")
        else:
            print(f"Dowland image, Status code: {response.status_code}")
    except Exception as e:
        print(f"Errro: {e}")
