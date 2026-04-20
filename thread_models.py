import threading
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


# ===== TASK FUNCTION =====
def task(thread_id, update_ui):
    update_ui(thread_id, "RUNNING")
    time.sleep(2)
    update_ui(thread_id, "TERMINATED")


# ===== MANY TO ONE =====
class ManyToOne:
    def __init__(self, update_ui):
        self.queue = Queue()
        self.update_ui = update_ui

        self.worker = threading.Thread(target=self.run)
        self.worker.daemon = True
        self.worker.start()

    def run(self):
        while True:
            thread_id = self.queue.get()
            task(thread_id, self.update_ui)

    def add_task(self, thread_id):
        self.queue.put(thread_id)


# ===== ONE TO ONE =====
class OneToOne:
    def __init__(self, update_ui):
        self.update_ui = update_ui

    def add_task(self, thread_id):
        t = threading.Thread(target=task, args=(thread_id, self.update_ui))
        t.start()


# ===== MANY TO MANY =====
class ManyToMany:
    def __init__(self, update_ui):
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.update_ui = update_ui

    def add_task(self, thread_id):
        self.executor.submit(task, thread_id, self.update_ui)