# Mô-đun request này giúp chúng ta thực hiện các yêu cầu HTTP tới URL
import requests

# Nhập URL cần lấy thông tin
url = input('Nhap URL: ')

# Gán giá trị cho biên userAgent
userAgent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

try:
    '''
        Biến res sẽ chứa response từ URL phản hồi về
        Để thực hiện 1 request tới URL chúng ta thực hiện request.get
            tham số đầu tiên sẽ là URL
            tham số thứ 2 sẽ truyền là headers = userAgent chúng ta vừa khởi tạo. Nếu để mặc định thì User-Agent sẽ là "python-requests/2.28.1"
            tham số thứ 3 truyền vào là thời gian timeout
    '''
    res = requests.get(url, headers=userAgent, timeout=5)

    print('Request header\n----------')
    # Vòng lặp này sẽ lặp qua từng phần tử header của request chúng ta gửi đi
    for i in res.request.headers:
        # In ra theo định dạng key: value
        print(i, ": ", res.request.headers[i])

    print('\nResponse header\n----------')
    # Vòng lặp này sẽ lặp qua từng phần tử header của response của server gửi về khi gửi resquest đi
    for i in res.headers:
        # In ra theo định dạng key: value
        print(i, ": ", res.headers[i])
except:
    # Nếu hết thời gian timeout hoặc là bị lỗi gì thì sẽ in ra dòng ERROR
    print('ERROR')