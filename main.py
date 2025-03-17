import os
import json
import nbtlib
from nbtlib.tag import String, Int, List, Compound

print("""
 █████  ███████ ██ ██      ██      ██ ███    ███  ██████  ███    ██  ██████  ██    ██ 
██   ██ ██      ██ ██      ██      ██ ████  ████ ██    ██ ████   ██ ██    ██ ██    ██ 
███████ █████   ██ ██      ██      ██ ██ ████ ██ ██    ██ ██ ██  ██ ██    ██ ██    ██ 
██   ██ ██      ██ ██      ██      ██ ██  ██  ██ ██    ██ ██  ██ ██ ██    ██  ██  ██  
██   ██ ██      ██ ███████ ███████ ██ ██      ██  ██████  ██   ████  ██████    ████   
""")

CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    print(f"Configuration file '{CONFIG_FILE}' not found!")
    exit(1)

with open(CONFIG_FILE, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

MINECRAFT_DIR = os.path.expandvars(os.path.expanduser(config["minecraft_directory"]))
SERVERS_FILE = os.path.join(MINECRAFT_DIR, config["servers_file"])
SERVERS_TXT = config["servers_txt"]


def load_servers_from_txt():
    if not os.path.exists(SERVERS_TXT):
        print(f"File '{SERVERS_TXT}' not found!")
        return []
    with open(SERVERS_TXT, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def load_existing_servers():
    if not os.path.exists(SERVERS_FILE):
        print(f"File '{SERVERS_FILE}' not found. A new one will be created.")
        return []
    try:
        return nbtlib.load(SERVERS_FILE)["servers"]
    except Exception as error:
        print(f"Error reading '{SERVERS_FILE}': {error}")
        return []


def update_servers_file(new_servers):
    existing_servers = load_existing_servers()
    existing_ips = {server["ip"]: server for server in existing_servers}

    new_servers = list(set(new_servers))

    added_count = 0
    for ip in new_servers:
        if ip not in existing_ips:
            server_entry = Compound({"hidden": Int(0), "ip": String(ip), "name": String(ip)})
            existing_servers.append(server_entry)
            added_count += 1

    nbtlib.File({"servers": List[Compound](existing_servers)}).save(SERVERS_FILE)

    print(f"Added {added_count} new servers. Total servers in file: {len(existing_servers)}.")


if __name__ == "__main__":
    servers = load_servers_from_txt()
    if servers:
        update_servers_file(servers)
