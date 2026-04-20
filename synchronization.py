import threading
import time


# ===== SEMAPHORE =====
class SemaphoreDemo:
    def __init__(self, update_ui):
        self.semaphore = threading.Semaphore(1)
        self.update_ui = update_ui

    def run(self, thread_id):
        self.update_ui(thread_id, "WAITING")

        with self.semaphore:
            self.update_ui(thread_id, "RUNNING")
            time.sleep(2)
            self.update_ui(thread_id, "TERMINATED")


# ===== MONITOR (LOCK) =====
class MonitorDemo:
    def __init__(self, update_ui):
        self.lock = threading.Lock()
        self.update_ui = update_ui

    def run(self, thread_id):
        self.update_ui(thread_id, "WAITING")

        with self.lock:
            self.update_ui(thread_id, "RUNNING")
            time.sleep(2)
            self.update_ui(thread_id, "TERMINATED")