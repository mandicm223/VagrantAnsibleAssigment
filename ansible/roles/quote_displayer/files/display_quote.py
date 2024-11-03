import os
import json
import random

# Directory containing the quote files
QUOTE_DIR = "/var/log/kanye_quotes"

def display_random_quote():
    # List all JSON files in the directory
    files = [f for f in os.listdir(QUOTE_DIR) if f.endswith(".json")]
    if not files:
        print("No quotes available.")
        return

    # Choose a random file and read its contents
    file_path = os.path.join(QUOTE_DIR, random.choice(files))
    with open(file_path, "r") as file:
        data = json.load(file)
        quote = data.get("quote", "No quote found.")
        print(f"Kanye Quote: {quote}")

if __name__ == "__main__":
    display_random_quote()
    print("Exiting container...")  # Exiting message
