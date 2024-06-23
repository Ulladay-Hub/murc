import os
from fetch import fetch_package
from decrypt import decrypt_package
from install import install_package
from utils import log

def yank_package(package_name, version):
    log("INFO", f"Fetching version {version} of package {package_name}")
    package_data = fetch_package(package_name, version)
    
    if not package_data:
        log("ERROR", f"Failed to fetch version {version} of package {package_name}")
        return
    
    log("INFO", "Decrypting package")
    decrypted_data = decrypt_package(package_data)
    
    if not decrypted_data:
        log("ERROR", f"Failed to decrypt package {package_name} version {version}")
        return
    
    log("INFO", "Installing the specified version")
    install_package(decrypted_data)
    
    log("INFO", f"Package {package_name} has been reverted to version {version}")
