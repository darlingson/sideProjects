import subprocess

bash_script = """
#!/usr/bin/expect -f
spawn sudo bash -c 'mv /home/darlingson/myfile.tx /var/'
expect "password for user:"
send "123456789\r"
interact
"""

with open('move_file.sh', 'w') as file:
    file.write(bash_script)

subprocess.call(['chmod', '+x', 'move_file.sh'])
subprocess.call(['./move_file.sh'])
