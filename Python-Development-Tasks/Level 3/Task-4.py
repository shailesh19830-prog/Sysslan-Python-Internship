import datetime

def write_log(message):
    # Get current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 'a' mode means append (adds to the end without deleting old logs)
    with open("system.log", "a") as file:
        file.write(f"[{current_time}] {message}\n")
    print(f"Log written: {message}")

write_log("User logged in successfully.")
write_log("Database backup completed.")