from bs4 import BeautifulSoup
import wget
import requests
import os
import urllib.request

url = "https://www.ybmbooks.com/reader/reader_read.asp?kind_sub=&step_1=&step_2=&category_1=366&id=2414&search=titlecontents&searchvalue=%B1%E2%C3%E2%B9%AE%C1%A6%C1%FD&page=1&seq=2841"
r = requests.get(url)
print(f"응답 : {r}")

soup = BeautifulSoup(r.text, "html.parser")
get_a_tag = soup.find_all("a")

download_path = "C:\\Users\\Caniro\\Desktop\\temp_downloads"
if not os.path.isdir(download_path):
    os.makedirs(download_path)

for get_link in get_a_tag:
    download_url = get_link.get('href')
    if "loadFile" in download_url:
        try:
            os.chdir(download_path)
            print(f"다운로드 주소 : {download_url}")
            # urllib.request.urlretrieve(url)
        except Exception as e:
            print(e)
            break
