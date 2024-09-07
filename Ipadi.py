import subprocess
import sys

def print_ascii_art():
    # ANSI escape codes for colors
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
    ascii_art = f"""
{GREEN} 
  _   _            _    __     __  _   _ 
 | | | | ___   ___| |_  \ \   / / | |_(_)
 | |_| |/ _ \ / __| __|  \ \ / /  | __| |
 |  _  |  __/ \__ \ |_    \ V /   | |_| |
 |_| |_|\___| |___/\__|    \_/     \__|_|
                                         
  ____                _   
 / ___|_ __ ___  __ _| |_ 
| |  _| '__/ _ \/ _` | __|
| |_| | | |  __/ (_| | |_ 
 \____|_|  \___|\__,_|\__|
{RESET}
"""
    print(ascii_art)

def scan_network(target):
    # Running masscan as a subprocess and capturing the output
    try:
        print("Scanning...")
        # Using masscan for faster scanning
        result = subprocess.run(['masscan', '-p1-65535', '--rate=1000', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print masscan's output
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error occurred: {result.stderr}")

        # Show the exit code
        print(f"masscan exit code: {result.returncode}")

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
