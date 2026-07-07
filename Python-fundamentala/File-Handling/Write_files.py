# write_file.py
# Topic: Writing to Files

print("=== Writing to Files ===\n")

# Method 1: Write mode ('w') - overwrites file
with open("output.txt", "w") as file:   # 'with' auto-closes file
    file.write("This is the first line.\n")
    file.write("Python File Handling Tutorial\n")
    file.write(f"Current time: 2026\n")

print("✅ Data written to 'output.txt'")

# Method 2: Append mode ('a')
with open("output.txt", "a") as file:
    file.write("\n--- New Entry ---\n")
    file.write("This line was appended.\n")

print("✅ Additional data appended.")
