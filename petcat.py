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

                               '''))    