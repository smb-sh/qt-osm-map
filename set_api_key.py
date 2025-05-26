#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python set_api_key.py your_api_key")
        sys.exit(1)

    api_key = sys.argv[1]
    files = [
        "cycle", "cycle-hires", "hiking", "hiking-hires",
        "night-transit", "night-transit-hires", "satellite",
        "street", "street-hires", "terrain", "terrain-hires",
        "transit", "transit-hires"
    ]

    for file in files:
        if os.path.isfile(file):
            with open(file, 'r') as f:
                content = f.read()
            new_content = content.replace("YOUR_API_KEY", api_key)
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Updated API key in {file}")
        else:
            print(f"File {file} not found. Skipping.")

if __name__ == "__main__":
    main()
