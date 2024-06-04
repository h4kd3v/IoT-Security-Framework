import hashlib
from utils.logger import log

def check_firmware_integrity(firmware_path, known_hash):
    with open(firmware_path, 'rb') as f:
        firmware_data = f.read()
        firmware_hash = hashlib.sha256(firmware_data).hexdigest()
        if firmware_hash == known_hash:
            log("Firmware integrity verified")
            return True
        else:
            log("Firmware integrity compromised")
            return False

if __name__ == "__main__":
    firmware_path = "path/to/firmware.bin"
    known_hash = "known_good_hash"
    check_firmware_integrity(firmware_path, known_hash)
