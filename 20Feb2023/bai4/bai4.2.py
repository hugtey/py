import nmap


class NmapScanner:
    def __init__(self):
        self.portScanner = nmap.PortScanner()

    def nmapScan(self, host, port):
        self.portScanner.scan(host, port)
        host = self.portScanner.all_hosts()[0]
        protocol = self.portScanner[host].all_protocols()[0]
        print('Port : %s State : %s' % (port,self.portScanner[host][protocol][int(port)]['state']))

def main():
    # nhập vào thông tin host cần scan
    host = input("Enter Host: ")
    # nhập vào thông tin các port cần scan
    ports = input("Nhập vào danh sách port muốn scan (cách nhau bằng dấu ','): ")
    # tạo ra danh sách port
    ports = ports.split(",")
    # scan theo từng port
    for port in ports:
        NmapScanner().nmapScan(host=host, port=port)

if __name__ == "__main__":
    main()