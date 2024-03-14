import subprocess

cmd = input("Give me your command: ")

if len(cmd) > 2:
	print("Command is too long!")

try:
	cmdstring = [cmd, "flag.txt"]
	print(f"Executed command: {cmdstring}")
	result = subprocess.check_output(cmdstring, timeout=1)
except:
	result = b"No 😿"

print(result.decode())