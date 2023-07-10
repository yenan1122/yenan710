yimport time

def concentration_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    print(f"Concentration timer started for {minutes} minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time // 60}:{remaining_time % 60:02d}", end="\r")
        time.sleep(1)

    print("\nConcentration time is up!")

# Example usage: Set a concentration timer for 25 minutes
concentration_timer(25)
