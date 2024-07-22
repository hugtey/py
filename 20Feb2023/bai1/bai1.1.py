import requests
import json


# API key lấy ở trên web shodan.io sau khi đang nhập
SHODAN_API_KEY = "LTgyfgLiI4GP4llyhevaXqAqo7Gooq4c"
# Hàm có chức năng scan ip nhập vào
def shodanInfo(ip):

    try:
        # Gửi request API lên shodan ddeeer thực hiện check thoong tin ip
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minity=True").text
        result = json.loads(result)
        # Sau khi định dạng lại dữ liệu trả về cho đẹp thì thực hiện in ra kết quả
        print(result)
    except Exception as exception:
        # Nếu phần trên có bất kì lỗi nào thì thực hiện in ra thông tin lỗi
        result = {"error": exception}

def main():
    # Nhập vào ip cần kiểm tra
    ip = input("Enter ip: ")
    # Gọi hàm shodanInfo và truyền thông tin vào
    data = json.dumps(shodanInfo(ip), indent=4)
    # In ra định dạng json cho dữ liệu được lấy về
    print(data)

if __name__ == "__main__":
    main()
