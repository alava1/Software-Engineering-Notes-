# append_file.py
# Topic: Appending data to existing files

print("=== Append Mode Demo ===\n")

def log_message(message):
    """Append a message to log file"""
    with open("log.txt", "a") as file:
        file.write(f"{message}\n")

# Using the function
log_message("User logged in")
log_message("User completed conditional statements")
log_message("User is learning file handling")

print("✅ Messages logged to 'log.txt'")

# Reading the log file to verify
print("\nLog file content:")
try:
    with open("log.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No log file yet.")
