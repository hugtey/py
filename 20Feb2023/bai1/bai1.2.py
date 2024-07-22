import shodan

# API_KEY
SHODAN_API_KEY = "B2pejCvTYOtthqYSkcWX9x4FukhKFCJU"
api = shodan.Shodan(SHODAN_API_KEY)


def main():
    while True:
        query = input("Nhap vao du lieu can tim kiem tren shodan(nhap exit de thoat): ")
        
        if query == 'exit':
            break
        
        result = api.search(query)

        for service in result['matches']:
            print(service['ip_str'])

if __name__ == "__main__":
    main()
