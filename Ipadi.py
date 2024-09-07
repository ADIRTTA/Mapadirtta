import subprocess
import sys

def scan_network(target):
    # Running nmap as a subprocess and capturing the output
    try:
        print(f"Scanning {target} ...")
        result = subprocess.run(['nmap', '-p-', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if nmap ran successfully
        if result.returncode == 0:
            print(result.stdout)  # Print nmap's output
        else:
            print(f"Error occurred: {result.stderr}")  # Print any error that occurred

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Check if user provided target as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python adi.py <target>")
        sys.exit(1)
    
    # Get the target from the command-line argument
    target = sys.argv[1]
    
    # Perform network scan
    scan_network(target)

if __name__ == "__main__":
    main()
    print(f"CODE BY ADIRTTA")
