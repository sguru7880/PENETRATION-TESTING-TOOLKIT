import sys
from port_scanner import port_scan
from brute_force import brute_force_login

def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Force (Simulated)")
    choice = input("Choose a module (1/2): ")

    if choice == "1":
        ip = input("Enter target IP: ")
        ports = input("Enter ports (comma-separated, e.g., 21,22,80): ")
        ports = [int(p.strip()) for p in ports.split(",")]
        port_scan(ip, ports)

    elif choice == "2":
        username = input("Enter username: ")
        wordlist_path = input("Enter path to wordlist (e.g., wordlist.txt): ")
        brute_force_login(username, wordlist_path)

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
