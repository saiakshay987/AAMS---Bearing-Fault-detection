from fault_detection.logging.logger import logging
from fault_detection.exception.exception import FaultdetectionException
import sys

if __name__ == "__main__":
    try:
        logging.info("Initializing system validation test...")
        print(">> Triggering a deliberate zero division to test exception tracking...")
        
        # This will deliberately crash and trigger our custom exception handler
        result = 1 / 0
        
    except Exception as e:
        # Wrap the core Python exception with your custom tracking context
        raise FaultdetectionException(e, sys)