import time
import os

def shutdown_timer(minutes):
    seconds = minutes * 60
    print(f"Shutdown timer set for {minutes} minutes.")
    
    for remaining_time in range(seconds, 0, -1):
        minutes_remaining = remaining_time // 60
        seconds_remaining = remaining_time % 60
        time_remaining = f"{minutes_remaining:02d}:{seconds_remaining:02d}"

        print(f"\rTime remaining: {time_remaining}", end="")
        time.sleep(1)
    
    print("\nShutting down...")
    os.system("shutdown /s /t 1")

if __name__ == "__main__":
    try:
        minutes = int(input("Enter the shutdown time in minutes: "))
        shutdown_timer(minutes)
    except ValueError:
        print("Please enter a valid number of minutes.")
