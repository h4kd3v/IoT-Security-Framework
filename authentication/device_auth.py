from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from utils.crypto_utils import load_public_key, load_private_key
from utils.logger import log

def authenticate_device(device_id, signature, public_key_path):
    public_key = load_public_key(public_key_path)
    try:
        public_key.verify(
            signature,
            device_id.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        log("Authentication successful")
        return True
    except Exception as e:
        log(f"Authentication failed: {e}")
        return False

if __name__ == "__main__":
    device_id = "device123"
    signature = b"..."
    public_key_path = "path/to/public_key.pem"
    authenticate_device(device_id, signature, public_key_path)
