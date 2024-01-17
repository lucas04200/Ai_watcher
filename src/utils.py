import os
import requests
import tarfile

import os
import requests
import tarfile

def download_and_extract_model(url, save_path, name_dir):
    # Create the directory with the custom name
    os.makedirs(os.path.join(save_path, name_dir), exist_ok=True)

    # Download the tar.gz file
    response = requests.get(url)

    # Specify the local destination where you want to save the tar.gz file
    local_destination = os.path.join(save_path, name_dir, "model.tar.gz")

    with open(local_destination, 'wb') as f:
        f.write(response.content)

    # Extract the contents of the tar.gz file
    with tarfile.open(local_destination, 'r:gz') as tar:
        tar.extractall(path=os.path.join(save_path, name_dir))

    os.remove(local_destination)
