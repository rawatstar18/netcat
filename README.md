# Netcat Automation Script

This script is designed to automate the process of performing a netcat (nc) check between servers using SSH. It leverages the `paramiko` library to establish SSH connections and execute commands remotely.

---

## Features
- Connect to multiple servers using SSH.
- Execute netcat (nc) commands to check connectivity between specified servers.
- Handles authentication errors and other exceptions gracefully.

---

## Requirements

1. Python 3.x
2. `paramiko` library

To install `paramiko`, run the following command:
```bash
pip install paramiko
```

---

## Configuration

### Common Credentials
Update the `user` and `password` variables in the script with your SSH username and password:
```python
user = "your_user_name"
password = "your_password"
```

### Server Configurations
Add your server configurations in the `configarutions` dictionary. Each entry should have the following structure:
```python
configarutions = {
    "testserver" : {"server":"192.168.0.1","server2":"192.168.63.6","port":"77777"},
    "testserver1" : {"server":"192.168.0.2","server2":"172.19.13.7","port":"77777"},
    # Add more servers as needed
}
```
- `server`: The SSH target server.
- `server2`: The server to perform the netcat check against.
- `port`: The port to test using netcat.

---

## Usage

### Running the Script
1. Save the script to a file, e.g., `netcat_automation.py`.
2. Run the script using Python:
   ```bash
   python netcat_automation.py
   ```
3. The script will prompt you to select a market (server configuration):
   ```bash
   Which Market do you want to netcat:
   ```
   Type the name of the server (e.g., `testserver`) and press Enter.

### Example Output
If the netcat command succeeds, you'll see the output from the server:
```
Connection to 192.168.63.6 77777 port [tcp/*] succeeded!
```
If there's an error, the error message will be displayed:
```
ssh error: Connection timed out
```

---

## Functions

### `pankaj(server, server2, port)`
- Connects to the target server via SSH.
- Executes the netcat (nc) command to test connectivity.
- Prints the command output or any errors encountered.

### `main()`
- Prompts the user to select a market/server.
- Fetches the server configuration from the `configarutions` dictionary.
- Calls the `pankaj()` function with the selected server details.

---

## Error Handling
- **AuthenticationException**: Handles incorrect SSH credentials.
- **SSHException**: Handles other SSH-related errors.
- **General Exception**: Catches any unexpected errors and prints the error message.

---

## Notes
- Ensure that the user has the necessary permissions to execute netcat commands on the target server.
- This script is for educational and internal use only. Use it responsibly and ensure compliance with your organization's policies.

---

## License
This script is open-source and distributed under the MIT License.

