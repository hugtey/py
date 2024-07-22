import socket
import platform
#Module platform trong Python là một module cung cấp các hàm để lấy thông tin về hệ điều hành và kiến trúc máy tính của bạn
import os
#Module os cung cấp các hàm để lấy thông tin về hệ điều hành, tên máy tính, thông tin về tài nguyên hệ thống
import psutil
#Module psutil cung cấp các hàm để lấy thông tin về việc sử dụng tài nguyên của hệ thống, như sử dụng CPU, bộ nhớ, dung lượng đĩa, v.v.

def get_system_info():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    system = platform.system()
    release = platform.release()
    version = platform.version()
    architecture = platform.machine()
    cpu_count = psutil.cpu_count()
    memory = psutil.virtual_memory()

    print("Hostname: " + hostname)
    print("IP Address: " + IPAddr)
    print("Operating System: " + system)
    print("Release: " + release)
    print("Version: " + version)
    print("Architecture: " + architecture)
    print("Number of CPUs: " + str(cpu_count))
    print("Memory Information: " + str(memory))

if __name__ == '__main__':
    get_system_info()
#Hàm get_system_info() là một hàm trong ví dụ trước đó tôi giải thích, nó thu thập các thông tin về hệ thống như tên máy, địa chỉ IP, 
# hệ điều hành, phiên bản, kiến trúc, số lượng CPU, thông tin bộ nhớ và in kết quả ra màn hình