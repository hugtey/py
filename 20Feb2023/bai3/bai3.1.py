# khai báo thư viện requests để thực hiện gửi requets lên server cần test
import requests
# khai báo thư viện os.path để thực hiện với bài này là thực hiện check xem file đã tồn tại hay chưa
import os.path

# hàm thực hiện chức năng fuzzing
def brute_force(url):
    logins = []
    # check xem thông tin file logins.txt có tồn tại trên thư mục không
    if os.path.exists("logins.txt") == False:
        # nếu file không tồn tại thì thực hiện tạo file
        with open("logins.txt", "wb") as f:
            # thực hiện lấy nội dung file từ trên github về để phục vụ công việc fuzzing login
            res = requests.get("https://raw.githubusercontent.com/fuzzdb-project/fuzzdb/master/discovery/predictable-filepaths/login-file-locations/Logins.txt")
            # ghi thông tin nội dung lấy đưuọc vào file logins.txt
            f.write(res.text.encode())
            f.close()
    # mở file và thực hiện lấy thông tin nội dung từng dòng của file cho vào mảng login để chuẩn bị thực hiện fuzzing
    with open("logins.txt", "r") as f:
        for line in f:
            logins.append(line[:-1])

    # Bắt đầu fuzzing
    for login in logins:
        # gửi từng request cùng với path login lên url
        res = requests.get(url + login)
        # nếu status code trả về là 200 thì đã tìm được đường dẫn để login
        if res.status_code == 200:
            print("Login resource detect: " + login)

def main():
    # nhập thông tin url muốn brute force
    url = input("Enter: ")
    # bắt đầu thực hiện fuzzing
    brute_force(url)

if __name__ == "__main__":
    main()