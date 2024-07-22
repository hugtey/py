import socket

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
server_address = ('localhost', 130)
client_socket.connect(server_address)

# Gửi dữ liệu cho server
message = b'Hello, Server!'
client_socket.sendall(message)

# Nhận dữ liệu từ server
data = client_socket.recv(1024)

# In dữ liệu nhận được
print("Dữ liệu nhận được:", data)

# Đóng kết nối
client_socket.close()