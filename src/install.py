import os
import tarfile
from utils import log, ensure_dir, load_config

def install_package(decrypted_data):
    config = load_config()
    package_directory = config["package_directory"]

    package_temp_file = 'temp_package.tar.gz'
    with open(package_temp_file, 'wb') as f:
        f.write(decrypted_data)

    log("INFO", "Extracting package")
    try:
        with tarfile.open(package_temp_file, 'r:gz') as tar:
            tar.extractall(path=package_directory)
        os.remove(package_temp_file)
        log("INFO", "Package installed successfully")
    except Exception as e:
        log("ERROR", f"Failed to extract package: {e}")
