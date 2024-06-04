from scapy.all import sniff
from sklearn.ensemble import IsolationForest
import numpy as np
from tensorflow.keras.models import load_model
from utils.logger import log

model = IsolationForest(contamination=0.1)
deep_model = load_model("path/to/deep_learning_model.h5")

def extract_features(packet):
    return [len(packet), packet.time]

def detect_anomalies(packet):
    features = np.array(extract_features(packet)).reshape(1, -1)
    isolation_prediction = model.predict(features)
    deep_prediction = deep_model.predict(features)

    if isolation_prediction == -1 or deep_prediction < 0.5:
        log("Anomaly detected!")
    else:
        log("Normal traffic")

def start_sniffing(interface="eth0"):
    sniff(iface=interface, prn=detect_anomalies, store=False)

if __name__ == "__main__":
    start_sniffing()
