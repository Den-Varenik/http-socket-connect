import socket
import http.client

# Define the Unix socket path
unix_socket_path = '/home/user/app-api/app.sock'

# Create a socket object
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to the Unix socket
sock.connect(unix_socket_path)

# Create an HTTPConnection object
conn = http.client.HTTPConnection('localhost')

# Set the socket object that the connection should use
conn.sock = sock

# Send an HTTP GET request to the API
conn.request('GET', '/api/endpoint')

# Get the HTTP response from the API
response = conn.getresponse()

# Read the response data
data = response.read()

# Print the response data
print(data)

# Close the HTTPConnection and socket objects
conn.close()
sock.close()

