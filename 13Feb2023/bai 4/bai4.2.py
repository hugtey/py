import requests


url = input("Enter url: ")

# Gửi request đến url và lấy về thông tin
res = requests.get(url)

# In ra header response 
print("Header response")
for header, value in res.headers.items():
    print(header + ": " + value)
#Trong mỗi lần lặp, header sẽ là tên của header, và value sẽ là giá trị của header. 
# Cách sử dụng này giúp lấy thông tin về các header trong một HTTP response.

# In ra header request
print("\nheader request")
for header, value in res.request.headers.items():
    print(header + ": " + value)
#Trong mỗi vòng lặp, header và value sẽ được gán bằng một cặp key-value tương ứng trong headers