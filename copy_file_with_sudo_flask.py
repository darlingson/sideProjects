import os


app = Flask(__name__)

@app.route('/')
def main():
    sudo_password = ''
    filenamme="filename.txt"
    destination = "/path/to/file"
    command = f'cp {filename} {destination}'
    os.system('echo %s | sudo -S %s' % (sudo_password,command))
    return "file copied"