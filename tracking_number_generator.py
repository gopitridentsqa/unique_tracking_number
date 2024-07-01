import uuid
from threading import Lock

class TrackingNumberGenerator:
    def __init__(self):
        self.used_ids = set()
        self.lock = Lock()
    
    def generate_tracking_number(self):
        while True:
            new_id = uuid.uuid4().hex
            with self.lock:
                if new_id not in self.used_ids:
                    self.used_ids.add(new_id)
                    return new_id
