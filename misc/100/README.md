# Connectivity Tester
User connects to the provided IP/port (via `netcat`) and enters their own IP/port (in the `IP:port` format). The challenge script will connect to the user-provided location and send a base64-encoded flag. To easily acquire the flag, the user can open a simple netcat listener (`nc -lvp 8888`) and provide their IP and port 8888 to the challenge script.

Flag: `flag{Th4nk5_0b4m4}`
