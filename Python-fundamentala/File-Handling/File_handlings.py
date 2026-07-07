# read_file.py
# Topic: Reading from Files

print("=== Reading Files ===\n")

# Method 1: Basic way (recommended for learning)
try:
    # Open file in read mode ('r')
    file = open("example.txt", "r")
    
    # Read entire content
    content = file.read()
    print("File Content:")
    print(content)
    
    # Always close the file
    file.close()
    
except FileNotFoundError:
    print("❌ Error: File 'example.txt' not found.")
    print("Creating a sample file first...")
    
    # Create sample file if it doesn't exist
    with open("example.txt", "w") as f:
        f.write("Hello Python Learners!\n")
        f.write("This is a sample file.\n")
        f.write("File handling is important.\n")
    
    print("✅ Sample file created. Run this script again.")
