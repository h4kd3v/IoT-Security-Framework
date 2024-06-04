from communication.mqtt_secure import setup_secure_mqtt
from communication.coap_secure import coap_request
from authentication.device_auth import authenticate_device
from anomaly_detection.anomaly_detector import start_sniffing
from firmware_analysis.firmware_checker import check_firmware_integrity
from web_interface.app import app
import threading
import asyncio

def main():
    mqtt_thread = threading.Thread(target=setup_secure_mqtt)
    mqtt_thread.start()

    coap_thread = threading.Thread(target=lambda: asyncio.run(coap_request()))
    coap_thread.start()

    auth_success = authenticate_device("device123", b"...", "path/to/public_key.pem")
    if auth_success:
        sniff_thread = threading.Thread(target=start_sniffing, args=("eth0",))
        sniff_thread.start()

    firmware_integrity = check_firmware_integrity("path/to/firmware.bin", "known_good_hash")
    if not firmware_integrity:
        print("Firmware integrity check failed")

    web_thread = threading.Thread(target=lambda: app.run(debug=True, use_reloader=False))
    web_thread.start()

if __name__ == "__main__":
    main()
