from SshToServer import SshToServer
import re
import csv
import os

my_ssh = SshToServer("/Users/ofek_matlov/Desktop/aws/my-key-pair.pem", "13.60.182.178", "ubuntu")
stdout, stdrr = my_ssh.runRemoteCommand("python3 python_script.py")
#print(stdout)
#print(stdrr)

def checkCommend(output : str ) -> str :
    stdout, stdrr = my_ssh.runRemoteCommand(output)
    if stdout != "":
        return stdout
    else:
        return "Error: " + stdrr 
checkCommend("python3 python_script.py")





