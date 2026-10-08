import collections
import threading

class MemoryRingBuffer:
    def __init__(self, max_size=500):
        # Initialize an optimized, fast thread-safe ring-buffer queue system
        self.max_size = max_size
        self.queue = collections.deque(maxlen=max_size)
        self.lock = threading.Lock()

    def push(self, data):
        """Pushes data objects safely into local RAM memory streams."""
        with self.lock:
            self.queue.append(data)

    def size(self):
        """Returns the current data packet volume resting inside the queue."""
        with self.lock:
            return len(self.queue)

    def flush_all(self):
        """Extracts and flushes all saved memory objects for cloud ingestion."""
        with self.lock:
            data_dump = list(self.queue)
            self.queue.clear()
            return data_dump
