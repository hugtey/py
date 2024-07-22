import nmap

# hàm thực hiện scan port
def ScanPort(host, ports):
    # khai báo object PortScanner()
    portScanner = nmap.PortScanner()
    # thực hiện scan với host nhập vào và các đối số port truyền vào
    portScanner.scan(hosts=host, arguments='-n -p ' + ports)
    # in ra command line của nmap
    print(portScanner.command_line())
    # lấy thông tin các host thực hiện scan
    hosts_list = [(x, portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
    # in ra tất cả các host thực hiện scan
    print(portScanner.all_hosts())
    # in ra thông tin các host và status
    for host, status in hosts_list:
        print(host, status)
    # in ra thông tin tất cả của các protocol
    for protocol in portScanner[host].all_protocols():
        print('Protocol : %s' % protocol)
        # in ra thông tin list port đã scan
        listport = portScanner[host][protocol]
        for port in listport:
            # In ra thông tin port và trạng thái của từng port
            print('Port : %s State : %s' % (port,portScanner[host][protocol][port]['state']))

def main():
    # nhập vào thông tin host
    host = input("Enter Host: ")
    # nhập vào thông tin port cần scan
    ports = input("Nhập vào danh sách port muốn scan (cách nhau bằng dấu ','): ")
    # bát đầu scan
    ScanPort(host, ports)

if __name__ == "__main__":
    main()