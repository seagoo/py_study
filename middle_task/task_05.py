# coding = utf-8
"""要求：批量抓取煎蛋网妹子栏目下的图片（http://jandan.net/ooxx）
 
主要涉及：网络请求、文件保存
"""
import urllib.request, urllib.error, re, time

def gethtml(url):
    try:
        page = urllib.request.urlopen(url)
        page_content = str(page.read())
        print(page_content)
        return page_content
    except urllib.error.herror as e:
        print(e.getcode())
        print(e.reason)
        print(e.geturl())


def getimage(page_content):
    print(type(page_content))
    reg = r'<img src="(.+?sinaimg.+?\.(jpg|gif))"'
    imgreg = re.compile(reg)
    img_urls = re.findall(imgreg, page_content)
    print(img_urls)
    i = 1
    global j
    for img_url in img_urls:
        print(img_url[0])
        if img_url[0][0:5] == 'http:':
            image = urllib.request.urlretrieve(img_url[0], r'd:\test123\%s.%s' % (str(j) + '-' + str(i), img_url[1]))
        else:
            image = urllib.request.urlretrieve('http:' + img_url[0], r'd:\test123\%s.%s' % (str(j) + '-' + str(i), img_url[1]))
        i += 1
        print(img_url)

page_num = int(input('请输入当前页数：'))
for j in reversed(range(1, page_num + 1)):
    print(r'http://jandan.net/ooxx/page-%s#comments' % j)
    getimage(gethtml(r'http://jandan.net/ooxx/page-%s#comments' % j))