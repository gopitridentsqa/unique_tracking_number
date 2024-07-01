import uuid
from threading import Lock

class TrackingNumberGenerator:
    def __init__(self):
        self.lock = Lock()
    
    def generate_tracking_number(self):
        while True:
            new_id = uuid.uuid4().hex
            with self.lock:               
                return new_id
