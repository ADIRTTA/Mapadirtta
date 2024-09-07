import subprocess
import sys

def print_ascii_art():
    print("""
   _ _    ____ ___ ____ _____ _____  _
   / \  |  _ \_ _|  _ \_   _|_   _|/ \
  / _ \ | | | | || |_) || |   | | / _ \
 / ___ \| |_| | ||  _ < | |   | |/ ___ \
/_/   \_\____/___|_| \_\|_|   |_/_/   \_\
""")

def scan_network(target):
    # Running nmap as a subprocess and capturing the output
    try:
        print("Scanning...")
        result = subprocess.run(['nmap', '-T5', '-p-', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print nmap's output
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error occurred: {result.stderr}")

        # Show the exit code
        print(f"nmap exit code: {result.returncode}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print_ascii_art()
    
    # Check if user provided target as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python network_scan.py <target>")
        sys.exit(1)
    
    # Get the target from the command-line argument
    target = sys.argv[1]
    
    # Perform network scan
    scan_network(target)

if __name__ == "__main__":
    main()
    print(f"CODE BY ADIRTTA")
