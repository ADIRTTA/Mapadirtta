import subprocess
import sys
import time

def print_ascii_art():
    # ANSI escape codes for colors
    GREEN = '\033[92m'
    RESET = '\033[0m'

    ascii_art = f"""
{GREEN}

             ___    ____  ________  _______________
            /   |  / __ \/  _/ __ \/_  __/_  __/   |       code by adirtta 😎
           / /| | / / / // // /_/ / / /   / / / /| |       THANK YOU FOR USE MY TOOL❤
          / ___ |/ /_/ // // _, _/ / /   / / / ___ |       don't copy my tool 🤗
         /_/  |_/_____/___/_/ |_| /_/   /_/ /_/  |_|     my github id: (github.com/ADIRTTA)

{RESET}
"""
    print(ascii_art)

def scan_network(target):
    # Running nmap as a subprocess and capturing the output
    try:
        print("Scanning...")
        # Start time for performance measurement
        start_time = time.time()

        # Using nmap for a fast scan
        # -T4: Set timing template to speed up scanning
        # -p1-65535: Scan all ports
        result = subprocess.run(['nmap', '-T5', '-p1-65535', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # End time for performance measurement
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Print nmap's output
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error occurred: {result.stderr}")

        # Show the exit code and performance
        print(f"nmap exit code: {result.returncode}")
        print(f"Scan completed in {elapsed_time:.2f} seconds.")

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
