import threading
import datetime
import os

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

                logs_dir = "/home/yana/atqc/ui_automation/logs"
                os.makedirs(logs_dir, exist_ok=True)

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                cls._instance.log_file = os.path.join(logs_dir, f"logs_{timestamp}.txt")

        return cls._instance

    def _write(self, level: str, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"[{timestamp}] [{level.upper()}] {message}"

        print(text)

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def info(self, message: str):
        self._write("info", message)

    def warn(self, message: str):
        self._write("warning", message)

    def error(self, message: str):
        self._write("error", message)
