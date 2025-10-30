import time

class FPSCounter:
    def __init__(self):
        self.prev_time = time.time()

    def get_fps(self):
        now = time.time()
        fps = 1.0 / max(1e-6, (now - self.prev_time))
        self.prev_time = now
        return fps
