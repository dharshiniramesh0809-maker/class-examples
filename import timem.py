import time

def countdown_timer(seconds):
    while seconds > 0:
        # Convert total seconds into MM:SS format
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02d}:{secs:02d}'
        
        # print with \r (carriage return) to overwrite the current line
        print(f"Time remaining: {timer_format}", end="\r")
        
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("\nTime's up!")

# Get user input and start
try:
    user_time = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_time)
except ValueError:
    print("Please enter a valid whole number.")