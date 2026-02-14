#Author: Ryan Grau
import sys

# Reads the contents text of the file
def read_file(file_name):
    """Read and return the contents of the specified file."""
    with open(file_name, 'r') as file:
        content = file.read()
    return content

# Displays the contents of the file
def display_file(content):
    """Display content in rows of 80 characters each."""
    for i in range(0, len(content), 80):
        print(content[i:i + 80])

# Calculates the checksum of the bits
def checksum_conversion(content, checksum_size):
    """Calculate checksum based on the specified bit size."""
    checksum = 0
    content_bytes = [ord(char) for char in content]
    
    # Padding the binary numbers
    if checksum_size == 16 and len(content_bytes) % 2 != 0:
        content_bytes.append(ord('X'))
    elif checksum_size == 32:
        while len(content_bytes) % 4 != 0:
            content_bytes.append(ord('X'))
            
    # Conditional operations to determine the bytes size then adding the values
    for byte in content_bytes:
        checksum += byte
        if checksum_size == 8:
            checksum &= 0xFF
        elif checksum_size == 16:
            checksum &= 0xFFFF
        elif checksum_size == 32:
            checksum &= 0xFFFFFFFF
    return checksum

#Output the checksum values
def main():
    if len(sys.argv) != 3:
        print("Usage: python pa02.py <filename> <checksum_size>")
        sys.exit(1)
        
    file_name = sys.argv[1]
    
    try:
        checksum_size = int(sys.argv[2])
    except ValueError:
        print("Checksum size must be an integer.", file=sys.stderr)
        sys.exit(1)
        
    if checksum_size not in [8, 16, 32]:
        print("Valid checksum sizes are 8, 16, or 32", file=sys.stderr)
        sys.exit(1)
        
    try:
        content = read_file(file_name)
    except FileNotFoundError:
        print(f"File not found: {file_name}", file=sys.stderr)
        sys.exit(1)
        
    display_file(content)
    checksum = checksum_conversion(content, checksum_size)
    char_count = len(content)
    
    print(f"{checksum_size} bit checksum is {checksum:0{checksum_size // 4}x} for all {char_count} chars")

if __name__ == "__main__":
    main()
