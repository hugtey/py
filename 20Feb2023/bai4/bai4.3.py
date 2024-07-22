import nmap
import json
# khai báo object portscan bất đồng bộ
portScannerAsync = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    # in ra thông tin sau khi đã scan
    print(scan_result)


def main():
    while True:
        # nhập vào thông tin để bắt đầu
        check = input("Nhap start de bat dau: ")
        # nếu thông tin nhập vào là start thì sẽ ngừng vòng lặp và thực hiện chạy scan
        if str.lower(check) == "start":
           break 
        # nhập vào thông tin host cần scan
        host = input("Nhap vao host: ")
        # nhập vào thông tin port cần scan
        ports = input("Nhap vap port can scan (cach nhau bang dau ,): ")
        # bắt đầu scan
        portScannerAsync.scan(hosts=host, arguments='-n -p ' + ports, callback=callback_result)
    while portScannerAsync.still_scanning():
        portScannerAsync.wait(None)

if __name__ == "__main__":
    main()