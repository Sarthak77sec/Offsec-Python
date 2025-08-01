#a netcat replacement from a python program
import argparse#an command line parsing library
import socket#module for network operations
import shlex#it takes commands as one piece
import subprocess#executes os commands from python file
import sys#it is an library to talk to the system and gets input from the system
import textwrap#formats long strings into clean code
import threading#performing multitasking using threads

def execute(cmd):
    cmd=cmd.strip()
    if not cmd:
        return
    output=subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)

    return output.decode()
if __name__ == '__main__':
    parser=argparse.ArgumentParser(
        description='BHP net TOOL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            petcat.py -t 192.168.108 -p 555 -l -c #command shell
            petcat.py -t 192.168.108 -p 555 -l -u=my.txt #upload a file                   
            petcat.py -t 192.168.108 -p 555 -l -e=\"cat /etc/passwd\" #execute a command
            echo 'ABC' | ./petcat.py -t 192.168.108 -p 135 #echo text to server port 135
            petcat.py -t 192.168.1.108 -p 555 #connect to server                                   
        '''))
parser.add_argument('-c', '--command', action='store_true', help='command shell')
parser.add_argument('-e', '--execute', help='execute specified command')
parser.add_argument('-l', '--listen', action='store_true', help='listen on which port')
parser.add_argument('-p', '--port', type=int, default=555, help='specified port')
parser.add_argument('-t', '--target', default='192.168.1.109',help='specify the target IP')
parser.add_argument('-u', '--upload', help='uplaod the file')
args=parser.parse_args()
if args.listen:#when listning the buffer will be empty cause we dont have to send the data immidiatly
    buffer= ''
else:
    buffer = sys.stdin.read()#else we will serve as a client and the buffer will store the commands from the command line output

pc=Petcat(args, buffer.encode())
pc.run()

#Petcat class that will hold the args
class Petcat:
    def __init__(self,args,buffer=None):
        self.args=args
        self.buffer=buffer
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()