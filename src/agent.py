import time
import random
import logging
from buffer import MemoryRingBuffer

# Configure professional enterprise diagnostic log output formats
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EdgeSyncAgent:
    def __init__(self):
        self.buffer = MemoryRingBuffer(max_size=500)
        self.network_stable = True
        logging.info("🛰️ High-Availability Operational Edge Sync Agent successfully activated.")

    def inspect_network_link(self):
        """Simulates automated health pings checking transit network stability."""
        # Randomly simulating an intermittent edge connection blackout block for execution testing
        if random.random() < 0.2:
            self.network_stable = not self.network_stable
            status = "STABLE" if self.network_stable else "DEGRADED/BLACKOUT DETECTED"
            logging.warning(f"📡 Cloud Connection Link State Shifted -> Status: {status}")

    def execute_pipeline_loop(self):
        """Runs the continuous telemetry collection and synchronization daemon loop."""
        iteration = 0
        logging.info("🚀 Data collection daemon loop running 24/7/365...")
        
        while True:
            iteration += 1
            self.inspect_network_link()
            
            # Generate a simulated real-world telemetry payload data object
            payload = {
                "node_id": "HA-EDGE-NODE-001",
                "timestamp": time.time(),
                "metric_payload_id": iteration,
                "system_health": "OK"
            }
            
            if self.network_stable:
                # Scenario A: Network is healthy. If the buffer has data, flush it first
                buffered_count = self.buffer.size()
                if buffered_count > 0:
                    logging.info(f"🔄 Network restored! Flushing {buffered_count} buffered packets to cloud vault...")
                    flushed_data = self.buffer.flush_all()
                    # Simulated database insertion ingestion
                    time.sleep(0.5) 
                    logging.info("🟢 Buffered data sync wave verified by cloud database registry.")
                
                logging.info(f"📤 Direct Transit: Synchronizing payload packet #{iteration} straight to Cloud Core.")
            else:
                # Scenario B: Network is dead. Divert payload immediately to local RAM buffer
                logging.info(f"📥 Connection Dead: Diverting data packet #{iteration} safely into Ring Buffer.")
                self.buffer.push(payload)
                logging.info(f"📊 Current offline memory queue size: {self.buffer.size()} packets.")
                
            time.sleep(2)

if __name__ == "__main__":
    agent = EdgeSyncAgent()
    try:
        agent.execute_pipeline_loop()
    except KeyboardInterrupt:
        logging.info("🛑 Edge Sync Agent loop safely intercepted and terminated by operator.")
