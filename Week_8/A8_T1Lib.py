from time import sleep

def activatePause(duration):
    print(f"Pausing for {duration} seconds.")
    sleep(duration)
    print("Unpaused")