from SshToServer import SshToServer
import os 
import time

def getArguments():
    name_file = input("Please enter the name of the file: ")
    second = int(input("how many second to wait ?"))
    return name_file, second
    
name_file,second = getArguments()    

my_ssh = SshToServer("/Users/ofek_matlov/Desktop/aws/my-key-pair.pem", "13.60.182.178", "ubuntu")
stdout, stdrr = my_ssh.runRemoteCommand(f"./server_bash.sh {name_file} {second}")
print(stdout)
print(stdrr)