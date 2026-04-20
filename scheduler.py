import time

class RoundRobinScheduler:
    def __init__(self, update_ui, log, quantum=2):
        self.update_ui = update_ui
        self.log = log
        self.quantum = quantum

    def run(self, total_threads):
        remaining = [3 for _ in range(total_threads)]  # burst time (fixed = 3)

        self.log("Starting Round Robin Scheduling")

        while any(r > 0 for r in remaining):
            for i in range(total_threads):
                if remaining[i] > 0:
                    self.update_ui(i + 1, "RUNNING")
                    self.log(f"Thread {i+1} running for {self.quantum}s")

                    time.sleep(self.quantum)

                    remaining[i] -= 1

                    if remaining[i] <= 0:
                        self.update_ui(i + 1, "TERMINATED")
                        self.log(f"Thread {i+1} finished")
                    else:
                        self.update_ui(i + 1, "READY")