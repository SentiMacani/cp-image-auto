import signal
import time
import threading
from functools import wraps

## Threading Controls Manager

# Global flag to signal all threads to stop 
# You have to pass around this flag to whoever is holding the runtime
stop_flag = threading.Event()
active_drivers = []

def signal_handler(signum, frame):
    print("\nCtrl+C pressed. Stopping all threads...")
    stop_flag.set()
    # close_all_drivers(active_drivers)

# Set up the signal handler
signal.signal(signal.SIGINT, signal_handler)

# def close_all_drivers(active_drivers):
#     for driver in active_drivers:
#         try:
#             teardown_driver(driver)
#         except Exception as e:
#             print(f"Error closing driver: {e}")
#     # Clear the list of active drivers
#     active_drivers.clear()
#     print("All Appium drivers have been closed.")

def signal_handling_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print(f"\nKeyboard interrupt received in {func.__name__}. Stopping...")
            stop_flag.set()
    return wrapper


def safe_sleep(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining = end_time - time.time()
        if remaining <= 0:
            break
        try:
            # Sleep in small increments to remain responsive
            threading.Event().wait(timeout=min(remaining, 0.1))
        except Exception:
            # If any exception occurs (including KeyboardInterrupt), 
            # check if we should stop
            if stop_flag.is_set():
                raise KeyboardInterrupt
    
    # Final check after sleep completes
    if stop_flag.is_set():
        raise KeyboardInterrupt
