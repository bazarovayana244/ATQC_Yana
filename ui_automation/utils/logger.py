import threading
import datetime
import os

class Logger:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Ensure initialization only happens once
        if not getattr(self, '_initialized', False):
            # Use a workspace-relative logs directory
            base_dir = os.path.dirname(os.path.abspath(__file__))
            logs_dir = os.path.join(base_dir, '..', 'logs')
            logs_dir = os.path.abspath(logs_dir)
            os.makedirs(logs_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.log_file = os.path.join(logs_dir, f"logs_{timestamp}.txt")
            self._initialized = True

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
