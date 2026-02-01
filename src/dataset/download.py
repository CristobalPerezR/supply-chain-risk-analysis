import os
import requests
from tqdm import tqdm

def download_dataset() -> str:
    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    csv_filename = os.path.join(raw_dir, "DataCoSupplyChainDataset.csv")

    url = "https://data.mendeley.com/public-files/datasets/8gx2fvg2k6/files/72784be5-36d3-44fe-b75d-0edbf1999f65/file_downloaded"

    if not os.path.exists(csv_filename):
        print("Downloading dataset...")
        
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='B', unit_scale=True)
        with open(csv_filename, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                t.update(len(data))
        t.close()
        
        print("Download finished.")
    else:
        print("CSV already exist, skipping download.")

    return csv_filename