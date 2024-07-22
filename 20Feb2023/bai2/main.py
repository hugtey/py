# https://www.geeksforgeeks.org/network-programming-in-python-dns-look-up/

import dns.resolver
# hàm thực hiện lấy thông tin dns của hostname
def get(hostName, a):
    try:
        # lấy thông tin hostname bằng hàm resolve 
        ip = dns.resolver.resolve(hostName, a)
    # nếu xảy ra lỗi thì gắn giá trị bằng error để thực hiện in ra
    except Exception as e:
        ip = ["error"]
    # in ra thông tin hostname đang test
    print(hostName)
    # in ra chế độ muốn lấy
    print(a)
    for i in ip:
        # in ra thông tin ip
        print(i)

def main():
    while True:
        # nhập vào hostname
        hostName = input("Nhap vao thong tin hostname (nhap exit de thoat): ")
        # nếu nhập vào chữ exit thì thực hiện thoát khỏi vòng lặp
        if str.lower(hostName) == "exit":
            break
        #  các thông tin cần lấy
        # MX: láy thông tin bản ghi  Mail Exchanger
        # A: lấy thông tin ipv4
        # AAAA: lấy thông tin ipv6
        # NS: lấy thông tin nameservice
        d = ["MX", "A", "AAAA", "NS"]
        for a in d:
            # gọi hàm và thực hiện scan
            get(hostName, a)

if __name__ == "__main__":
    main()