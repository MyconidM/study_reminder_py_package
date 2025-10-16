# logger.py
import datetime
import os

def log_reminder(student, reminder):
    """Log a sent reminder with a timestamp to a file."""
    # Get the directory where main.py is located (src folder)
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file_path = os.path.join(current_dir, "reminder_log.txt")
    
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}: {reminder}\n\n")

