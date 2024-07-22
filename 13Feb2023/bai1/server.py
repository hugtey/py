import socket

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gán địa chỉ và cổng cho socket
server_address = ('localhost', 130)
server_socket.bind(server_address)
#Phương thức bind() được sử dụng để liên kết ổ cắm máy chủ với một địa chỉ mạng cụ thể (tên máy chủ và số cổng).
#  Tham số server_address là một bộ chứa tên máy chủ và số cổng của ổ cắm. 
# Phương pháp này thường được gọi trước khi ổ cắm máy chủ được đặt ở trạng thái nghe.

# Chạy socket làm server
server_socket.listen(2)
print("Server đang chạy...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()
print("Kết nối từ", client_address)

# Nhận dữ liệu từ client
data = client_socket.recv(1024)
#client_socket.recv là phương thức của lớp socket trong Python, nó cho phép một chương trình client để nhận dữ liệu từ một máy chủ socket. 
# Phương thức này sẽ trả về một chuỗi nhị phân chứa dữ liệu đã nhận được từ máy chủ.

#Cú pháp của phương thức recv là: recv(bufsize, flags=0).
#  Tham số bufsize xác định kích thước tối đa của chuỗi dữ liệu sẽ nhận được từ máy chủ.

# Gửi dữ liệu cho client
client_socket.sendall(data)
#client_socket.sendall() là một phương thức của Python socket module cho phép gửi tất cả dữ liệu tới máy chủ từ một socket client. 
# Nó nhận vào một chuỗi dữ liệu và gửi tất cả dữ liệu đó cho máy chủ từ socket client. Nếu không thể gửi đủ dữ liệu, nó sẽ gửi lại lỗi.

# Đóng kết nối
client_socket.close()
server_socket.close()