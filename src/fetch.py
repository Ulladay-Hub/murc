import requests
from utils import log, load_config

def fetch_package(package_name, version=None):
    config = load_config()
    package_directory = config["package_directory"]

    # Load package metadata
    with open(f'{package_directory}/{package_name}/{package_name}.mrcpkg', 'r') as f:
        package_info = json.load(f)
    
    release_link = package_info["release_link"]
    if version:
        release_url = f"{release_link}/tag/{version}"
    else:
        release_url = f"{release_link}/latest"
    
    log("INFO", f"Fetching release from {release_url}")
    response = requests.get(release_url)
    
    if response.status_code == 200:
        log("INFO", "Package fetched successfully")
        return response.content
    else:
        log("ERROR", "Failed to fetch the package")
        return None
