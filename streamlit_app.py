import datetime
import time

def send_reminder(message):
    # Replace this with code to send reminders via your desired method (e.g., notifications, email)
    print(f"Reminder: {message}")

def schedule_reminders(reminder_times, messages):
    while reminder_times:  # Continue as long as there are remaining reminders
        current_time = datetime.datetime.now().time()
        for reminder_time in reminder_times:
            if current_time >= reminder_time:
                index = reminder_times.index(reminder_time)
                send_reminder(messages[index])
                # Remove the reminder that was just processed
                reminder_times.pop(index)
                messages.pop(index)
                break  # Restart the loop since we've modified the list
        time.sleep(60)  # Check the time every minute

# Example usage
reminder_times = [
    datetime.time(9, 0),   # Customize these to your preferred exercise times
    datetime.time(14, 0),
    datetime.time(18, 30)
]

messages = [
    "Time to hit the gym!",
    "Take a break and stretch.",
    "Go for a jog!"
]

schedule_reminders(reminder_times, messages)

