import urllib.request as req
import re

# 웹 페이지 접속
url = 'https://daum.net'
headers = {'User-Agent': 'Mozilla/5.0'}  # 브라우저인 것처럼 헤더 추가
request = req.Request(url, headers=headers)
response = req.urlopen(request)

# 웹 페이지 내용 읽기
data = response.read().decode('utf-8')

# 이미지 URL 찾기 (jpg, jpeg, png 등 이미지 확장자 포함)
result = re.findall(r'https://[^\s<>"\']+?(?:jpg|jpeg|png|gif)', data)

# 이미지 다운로드
for link in result:
    try:
        # 파일명 추출
        filename = link.split('/')[-1]
        print(f"Downloading: {filename}")
        
        # 이미지 다운로드
        request = req.Request(link, headers=headers)
        with req.urlopen(request) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
                
    except Exception as e:
        print(f"Error downloading {link}: {str(e)}")

