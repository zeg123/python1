import requests
from lxml import html

url = 'http://aoqi.100bt.com/version4/jingling/daquan_list.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
res = response.text
# print(res)
info = html.etree.HTML(res)
items = info.xpath('//div[@class="aoqiJingling daquan"]//ul[@class="daquanList clearfix lazyloadItem"]/li[@class="daquanItem pr"]')
for item in items:
    name = item.xpath('.//a/span[@class="ttell"]/text()')[0]
    img = item.xpath('.//a/div[@class="wimg"]/img/@src')
    print(name,img)
    # res1 = requests.get(img,headers=headers)
    # with open(f'D:/aoqi/{name}.jpg', 'wb') as f:
    #     f.write(res1.content)
