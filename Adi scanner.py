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
    # ANSI escape codes for colors
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    # Running nmap as a subprocess and capturing the output
    try:
        print(f"{GREEN}Scanning...{RESET}")
        # Start time for performance measurement
        start_time = time.time()

        # Using nmap with optimizations
        # -T4: Timing template to speed up scanning
        # -p1-1000: Scan the most common 1000 ports
        result = subprocess.run(['nmap', '-T4', '-p1-1000', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # End time for performance measurement
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Print nmap's output with color
        if result.returncode == 0:
            print(f"{GREEN}{result.stdout}{RESET}")
        else:
            print(f"{RED}Error occurred: {result.stderr}{RESET}")

        # Show the exit code and performance
        print(f"{GREEN}nmap exit code: {result.returncode}{RESET}")
        print(f"{GREEN}Scan completed in {elapsed_time:.2f} seconds.{RESET}")

    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")

def main():
    print_ascii_art()

    # Prompt the user for the target IP address
    target = input("Enter the IP address or hostname to scan: ").strip()

    # Perform network scan
    scan_network(target)

if __name__ == "__main__":
    main()
