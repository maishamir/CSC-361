from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.uvic.ca'
port = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
print('HELO COMMAND\r\n')
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
print('MAIL FROM COMMAND\r\n')
clientSocket.send('MAIL FROM: <maisha.mir2012@gmail.com>\r\n')
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
print('RCPT TO COMMAND\r\n')
clientSocket.send('RCPT TO: <maisha.mir2014@gmail.com>\r\n')
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response. 
print("DATA COMMAND\r\n")
clientSocket.send('DATA\r\n')
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('354 reply not received from server.')

# Send message data.
print('SEND MESSAGE DATA\r\n')
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)

# Send QUIT command and get server response.
print('QUIT COMMAND\r\n')
clientSocket.send('QUIT\r\n') #tells the server to terminate the connection
clientSocket.close()