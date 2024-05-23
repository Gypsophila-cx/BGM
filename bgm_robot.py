import requests             # requests


baseurl = 'http://bgm.tv/'  # Full domain name
filename = 'robots.txt'     # File name
# baseurl + filename = 'http://bgm.tv/robots.txt'

response = requests.get(baseurl + filename)  # Get方式获取网页数据
print(response.text)  # 输出