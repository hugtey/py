import requests
from bs4 import BeautifulSoup
import openpyxl

# Khởi tạo đối tượng workbook và worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Tiêu đề cột
ws.append(['MS phân bón', 'Tên phân bón', 'Số quyết định', 'Thời hạn', 'Loại phân bón', 'Nguồn gốc phân bón', 'Phương thức sử dụng', 'Hạn sử dụng', 'Tên chỉ tiêu - hàm lượng 1', '', 'Tên chỉ tiêu - hàm lượng 2', '', 'Tên chỉ tiêu - hàm lượng 3', '', 'Tên chỉ tiêu - hàm lượng 4', '', 'Tên chỉ tiêu - hàm lượng 5', '', 'Tên chỉ tiêu - hàm lượng 6', '', 'Tên chỉ tiêu - hàm lượng 7', '', 'Tên chỉ tiêu - hàm lượng 8', '', 'Tên chỉ tiêu - hàm lượng 9', '', 'Tên chỉ tiêu - hàm lượng 10', '', 'Tên chỉ tiêu - hàm lượng 11', '', 'Tên chỉ tiêu - hàm lượng 12', '', 'Hướng dẫn sử dụng', 'Tên tổ chức', 'Địa chỉ', 'Điện thoại', 'MS doanh nghiệp'])

# Vòng lặp lấy dữ liệu từ mã số 00001 đến 10
for i in range(1, 30011):
    # Chuyển đổi mã số thành chuỗi có 5 ký tự
    ma_so = f"{i:05d}"
    response = requests.get(f"http://113.190.254.147/PhanBon/en/phanbonchungnhan?CongNhanPhanBonID=3823&TenPhanBon=&MaPhanBon={ma_so}&Key=0&SoQuyetDinh=")

    if response.status_code == 200:
        try:
            # Phân tích HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # Lấy thông tin phân bón từ HTML

            # Tên phân bón
            element_phanbon = soup.find('div', class_='col-md-6 tdPhanBon')
            if element_phanbon:
                tenphanbon = element_phanbon.find('h3').text.strip()
            else:
                tenphanbon = None

            # Số quyết định
            soquyetdinh_element = soup.find('a', class_='btnSoQuyetDinh')
            if soquyetdinh_element:
                soquyetdinh = soquyetdinh_element.text.strip()
            else:
                soquyetdinh = None

            # Thời hạn
            lis = soup.find_all('li', style='list-style: none;')
            if len(lis) >= 3:
                thoihan = lis[2].text.strip()
            else:
                thoihan = None

            # Loại phân bón
            divs = soup.find_all('div', class_='col-md-6')
            spans = soup.find_all('span')
            if len(divs) >= 2 and len(spans) >= 2:
                loaiphanbon = divs[1].find_all('span')[0].text.strip()
            else:
                loaiphanbon = None

            # Nguồn gốc phân bón
            if len(divs) >= 2 and len(spans) >= 2:
                nguongocphanbon = divs[1].find_all('span')[1].text.strip()
            else:
                nguongocphanbon = None

            # Phương thức sử dụng
            if len(divs) >= 2 and len(spans) >= 2:
                phuongthucsudung = divs[1].find_all('span')[2].text.strip()
            else:
                phuongthucsudung = None

            # Hạn sử dụng
            if len(divs) >= 2 and len(spans) >= 2:
                hansudung = divs[1].find_all('span')[-1].text.strip()
            else:
                hansudung = None

            # Tên chỉ tiêu và Hàm lượng
            tds = soup.find_all('td')
            if len(divs) >= 3 and len(tds) >= 3:
                tenchitieu1 = divs[2].find_all('td')[1].text.strip()
                hamluong1 = divs[2].find_all('td')[2].text.strip()
            else:
                tenchitieu1 = None
                hamluong1 = None

            tds = soup.find_all('td')
            if len(divs) >= 3 and len(tds) >= 3:
                tenchitieu2 = divs[2].find_all('td')[4].text.strip()
                hamluong2 = divs[2].find_all('td')[5].text.strip()
            else:
                tenchitieu2 = None
                hamluong2 = None
            
            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu3 = divs[2].find_all('td')[7].text.strip()
                except IndexError:
                    tenchitieu3 = None
    
                try:
                    hamluong3 = divs[2].find_all('td')[8].text.strip()
                except IndexError:
                    hamluong3 = None
            else:
                tenchitieu3 = None
                hamluong3 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu4 = divs[2].find_all('td')[10].text.strip()
                except IndexError:
                    tenchitieu4 = None
    
                try:
                    hamluong4 = divs[2].find_all('td')[11].text.strip()
                except IndexError:
                    hamluong4 = None
            else:
                tenchitieu4 = None
                hamluong4 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu5 = divs[2].find_all('td')[13].text.strip()
                except IndexError:
                    tenchitieu5 = None
    
                try:
                    hamluong5 = divs[2].find_all('td')[14].text.strip()
                except IndexError:
                    hamluong5 = None
            else:
                tenchitieu5 = None
                hamluong5 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu6 = divs[2].find_all('td')[16].text.strip()
                except IndexError:
                    tenchitieu6 = None
    
                try:
                    hamluong6 = divs[2].find_all('td')[17].text.strip()
                except IndexError:
                    hamluong6 = None
            else:
                tenchitieu6 = None
                hamluong6 = None
            
            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu7 = divs[2].find_all('td')[19].text.strip()
                except IndexError:
                    tenchitieu7 = None
    
                try:
                    hamluong7 = divs[2].find_all('td')[20].text.strip()
                except IndexError:
                    hamluong7 = None
            else:
                tenchitieu7 = None
                hamluong7 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu8 = divs[2].find_all('td')[22].text.strip()
                except IndexError:
                    tenchitieu8 = None
    
                try:
                    hamluong8 = divs[2].find_all('td')[23].text.strip()
                except IndexError:
                    hamluong8 = None
            else:
                tenchitieu8 = None
                hamluong8 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu9 = divs[2].find_all('td')[25].text.strip()
                except IndexError:
                    tenchitieu9 = None
    
                try:
                    hamluong9 = divs[2].find_all('td')[26].text.strip()
                except IndexError:
                    hamluong9 = None
            else:
                tenchitieu9 = None
                hamluong9 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu10 = divs[2].find_all('td')[28].text.strip()
                except IndexError:
                    tenchitieu10 = None
    
                try:
                    hamluong10 = divs[2].find_all('td')[29].text.strip()
                except IndexError:
                    hamluong10 = None
            else:
                tenchitieu10 = None
                hamluong10 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu11 = divs[2].find_all('td')[31].text.strip()
                except IndexError:
                    tenchitieu11 = None
    
                try:
                    hamluong11 = divs[2].find_all('td')[32].text.strip()
                except IndexError:
                    hamluong11 = None
            else:
                tenchitieu11 = None
                hamluong11 = None

            if len(divs) >= 3 and len(tds) >= 3:
                try:
                    tenchitieu12 = divs[2].find_all('td')[34].text.strip()
                except IndexError:
                    tenchitieu12 = None
    
                try:
                    hamluong12 = divs[2].find_all('td')[35].text.strip()
                except IndexError:
                    hamluong12 = None
            else:
                tenchitieu12 = None
                hamluong12 = None

            # Hướng dẫn sử dụng
            if len(divs) >= 4 and len(tds) >= 3:
                huongdansudung = divs[3].find_all('td')[-1].text.strip()

            # Tên tổ chức
            if len(divs) >= 4 and len(tds) >= 3:
                tentochuc = divs[4].find_all('td')[1].text.strip()

            # Địa chỉ
            if len(divs) >= 4 and len(tds) >= 3:
                diachi = divs[4].find_all('td')[3].text.strip()
            
            # Điện thoại
            if len(divs) >= 4 and len(tds) >= 3:
                dienthoai = divs[4].find_all('td')[5].text.strip()
            
            # MS doanh nghiệp
            if len(divs) >= 4 and len(tds) >= 3:
                MSdoanhnghiep = divs[4].find_all('td')[7].text.strip()
            
            # Ghi dữ liệu vào Excel
            ws.append([ma_so, tenphanbon, soquyetdinh, thoihan, loaiphanbon, nguongocphanbon, phuongthucsudung, hansudung, tenchitieu1, hamluong1, tenchitieu2, hamluong2, tenchitieu3, hamluong3, tenchitieu4, hamluong4, tenchitieu5, hamluong5, tenchitieu6, hamluong6,tenchitieu7, hamluong7, tenchitieu8, hamluong8,tenchitieu9, hamluong9, tenchitieu10, hamluong10, tenchitieu11, hamluong11, tenchitieu12, hamluong12, huongdansudung, tentochuc, diachi, dienthoai, MSdoanhnghiep])

            print(f"Lấy dữ liệu cây {i} thành công")
        
        except AttributeError as e:
            print(f"Lỗi khi lấy dữ liệu cây {i}: Không tìm thấy thông tin - {str(e)}")
            continue  # Bỏ qua lỗi và tiếp tục vòng lặp nếu có lỗi cụ thể này
        
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu cây {i}: {str(e)}")
            continue  # Bỏ qua các lỗi khác và tiếp tục vòng lặp nếu có lỗi
        
    else:
        print(f"Lỗi khi lấy dữ liệu cây {i}: {response.status_code}")
        continue  # Bỏ qua lỗi và tiếp tục vòng lặp nếu không thành công

# Lưu file Excel
wb.save('data_phan_bon.xlsx')
