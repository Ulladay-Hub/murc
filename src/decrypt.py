from cryptography.fernet import Fernet
from utils import log

# Not working yet. Still making logic
# SECRET_KEY = b'secret-key'

def decrypt_package(package_data):
    log("INFO", "Decrypting package")
    #cipher_suite = Fernet(SECRET_KEY)
    try:
        #decrypted_data = cipher_suite.decrypt(package_data)
        log("INFO", "Package decrypted successfully")
        return package_data
    except Exception as e:
        log("ERROR", f"Failed to decrypt package: {e}")
        return None
