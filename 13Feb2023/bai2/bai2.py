import socket

ip = '42.113.206.26'
ports = [21, 22, 23, 80, 443]
# Cổng 21 là cổng giao tiếp cho dịch vụ File Transfer Protocol (FTP).

#Cổng 22 là cổng giao tiếp cho dịch vụ Secure Shell (SSH).

#Cổng 23 là cổng giao tiếp cho dịch vụ Telnet.

#Cổng 80 là cổng giao tiếp cho dịch vụ Hypertext Transfer Protocol (HTTP).

#Cổng 443 là cổng giao tiếp cho dịch vụ Hypertext Transfer Protocol Secure (HTTPS).

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
        print("Cổng {} mở trên {}".format(port, ip))
    else:
        print("Cổng {} đóng trên {}".format(port, ip))
    s.close()