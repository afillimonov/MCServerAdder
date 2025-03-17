**[Версия на русском языке](https://github.com/afillimonov/MCServerAdder/blob/main/README-ru.md)**
# 🛠 Minecraft Server List Updater

This Python script help if you need to add a large numbers of servers to your server list at once.

---

## 🚀 **Functionality**

- **Load Servers from Text File**: Reads server IPs from a user-defined `.txt` file (e.g., `servers.txt`).
- **Update `servers.dat`**: Parses the Minecraft `servers.dat` file (NBT format) and adds new servers while avoiding duplicates.
- **Configuration Support**: Uses a `config.json` file to specify paths to the Minecraft directory, `servers.dat`, and the input text file.
- **Error Handling**: Gracefully handles missing files and errors during NBT parsing.
- **Cross-Platform**: Works on any system with Python installed.

---

## ⚙️ **Configuration**

The script relies on a `config.json` file to function properly. Below is an example configuration:

```json
{
  "minecraft_directory": "~/.minecraft",
  "servers_file": "servers.dat",
  "servers_txt": "servers.txt"
}
```
### **Fields Explained**

- **`minecraft_directory`**: Path to your Minecraft directory (e.g., `~//.minecraft` on Linux/macOS or `%APPDATA%\\.minecraft` on Windows).
- **`servers_file`**: Relative path to the `servers.dat` file within the Minecraft directory.
- **`servers_txt`**: Path to the text file containing server IPs, one per line.

---

## 📌 **Prerequisites**

1. **Python Version**: Python 3.10 or higher is required.
2. **Minecraft Version**: Compatible with Minecraft versions that use the `servers.dat` file in NBT format (most versions since 1.7.2).
3. **Dependencies**: Important to install the required library using pip:
   ```bash
   pip install nbtlib
   ```
## 🧱 **Steps to Run**

1. ### **Clone this repository**:
   ```bash
   git clone https://github.com/afillimonov/MCServerAdder.git
   cd MCServerAdder
   ```
2. ### **Prepare Servers List and Configuration**:

1. **Add Server IPs to `servers.txt`:**
   - Use the format: `IP:PORT` (one server per line).
   - **Example:**
     ```
      127.0.0.1
      1.2.3.4:25567
      example.com
      example.com:25567
     ```
   - If the port is not specified, the default port `25565` will be used automatically.

2. **Set the Correct Path to game in `config.json`:**
3. ### **Run the script**:
   ```bash
   python main.py
   ```
4. ### **Check your Minecraft client's server list to verify the updates.**
## **❓ Troubleshooting**
### **If you encounter any issues while using this script:**

1. **Ensure all paths in config.json are correct and accessible.**
2. **Verify that the servers.txt file exists and contains valid server IPs.**
3. **Check the console output for error messages and resolve them accordingly.**
