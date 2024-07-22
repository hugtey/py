import random

# Hàm tạo dữ liệu giả lập cho tuổi của các thành viên
def generate_age_data(num_members):
    ages = random.sample(range(20, 51), num_members)
    return ages

# Hàm sắp xếp thành viên theo quy tắc yêu cầu
def custom_sort_ages(ages):
    n = len(ages)
    for i in range(n):
        for j in range(0, n-i-1):
            if ages[j] > ages[j+1]:
                # Hoán đổi tuổi của các thành viên
                ages[j], ages[j+1] = ages[j+1], ages[j]
    sorted_ages = []
    for i in range(n//2):
        sorted_ages.append(ages[i])
        sorted_ages.append(ages[-(i+1)])
    if n % 2 != 0: # Trường hợp số lượng thành viên là số lẻ
        sorted_ages.append(ages[n//2])
    return sorted_ages

# Số lượng thành viên
num_members = 10

# Tạo dữ liệu giả lập cho tuổi của các thành viên
ages = generate_age_data(num_members)

# Sắp xếp thành viên theo quy tắc
sorted_ages = custom_sort_ages(ages)

print("Dữ liệu tuổi của các thành viên:")
print(ages)
print("Dữ liệu tuổi đã được sắp xếp theo quy tắc:")
print(sorted_ages)
