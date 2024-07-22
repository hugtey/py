# khai báo thư viện requests
import requests
# nhập vào url muốn test
url = input("Enter url: ")

# Gửi request với method get đến url
response = requests.get(url)

# Lấy về thông tin status code trả về và in ra khi thực hiện request lên url
status_code = response.status_code
# in ra thông tin status
print("Status Code:", status_code)

# In ra nội dung response nhận được khi thực hiện request đến url
data = response.text
print("Data:\n")
# in ra nội dung server trả về thành công
print(data)