import time

# Simulated login credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "letmein"

def brute_force_login(user, wordlist_file):
    print(f"[+] Starting Brute Force on user '{user}'")
    try:
        with open(wordlist_file, "r") as file:
            for line in file:
                password = line.strip()
                print(f"Trying password: {password}")
                time.sleep(0.5)  # simulate delay
                if password == VALID_PASSWORD:
                    print(f"[SUCCESS] Password found: {password}")
                    return True
        print("[FAILURE] Password not found in wordlist.")
    except FileNotFoundError:
        print("[ERROR] Wordlist file not found.")
    return False
