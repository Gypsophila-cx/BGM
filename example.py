from bs4 import BeautifulSoup           # 网页解析，获取数据
import re                               # 正则表达式，进行文字匹配
import urllib.request, urllib.error     # 制定URL，获取网页数据
import xlwt                             # 进行excel操作


gamename = '战女神M'
subjectname = '88429'  # 就是你要爬的内容的subject号
baseurl = "http://bgm.tv"  # bangumi链接
url = baseurl + "/subject/"+ subjectname +"/characters"  # 要爬取的网页链接
col = ("角色详情链接", "角色日文名", "角色中文名", "CV详情链接", "CV中译名")


# 创建正则表达式对象
findChara = re.compile(r'<h2>(.*?)</h2>')  # 角色信息
findCharaLink = re.compile(r'<a class="l" href="(.*?)">')  # 0.角色详情链接
findCharaJapanese = re.compile(r'">(.*?)</a>')  # 1.角色日文名
findCharaChinese = re.compile(r'<span class="tip"> / (.*?)</span>')  # 2.角色中文名
findCvLink = re.compile(r'<a class="avatar" href="(.*?)">')  # 3.CV详情链接
findCvName = re.compile(r'<small class="grey">(.*?)</small>')  # 4.CV名字


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，这段我抄的https://blog.csdn.net/bookssea/article/details/107309591
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    print("URL内容请求成功")
    return html


# 给链接添加baseurl前缀，如果为空就返回空，否则返回baseurl + content
def reshapeLink(content):
    if content == "":
        return ""
    else:
        return baseurl + content


# 如果正则表达式返回为空列表，则返回""，否则返回第0个元素
def getContent(content):
    if content == []:
        return ""
    else:
        return content[0]


# 爬取网页
def getData(url):
    datalist = []  # 用来存储爬取的网页信息
    html = askURL(url)  # 保存获取到的网页源码
    
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="light_odd"):  # 查找符合要求的字符串
        data = []  # 保存角色的对应信息

        # 通过正则表达式查找
        chara = re.findall(findChara, str(item))[0]  # 角色信息

        charalink = getContent(re.findall(findCharaLink, chara))  # 0.角色链接
        data.append(reshapeLink(charalink))
        charajapanese = getContent(re.findall(findCharaJapanese, chara))  # 1.角色中文名
        data.append(charajapanese)
        charachinese = getContent(re.findall(findCharaChinese, chara))  # 2.角色日文名
        data.append(charachinese)

        cv = getContent(item.find_all('div', class_="actorBadge clearit"))  # cv信息
        cvlink = getContent(re.findall(findCvLink, str(cv)))  # 3.cv链接
        data.append(reshapeLink(cvlink))
        cvname = getContent(re.findall(findCvName, str(cv)))  # 4.cv中译名
        data.append(cvname)
        

        # 将信息添加到datalist里去
        datalist.append(data)

    #print(datalist)
    return datalist

# 保存数据到表格
def saveData(datalist, savepath):
    print("save excel.......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建workbook对象
    sheet = book.add_sheet(gamename, cell_overwrite_ok=True) # 创建工作表
    
    for i in range(0, len(col)):
        sheet.write(0,i,col[i])  # 列名
    for i in range(0, len(datalist)):
        #print("第%d条" %(i+1))       # 输出语句，用来测试
        data = datalist[i]
        for j in range(0, len(col)):
            sheet.write(i+1,j,data[j])  # 数据
    book.save(savepath) # 保存


# 保存数据到txt
def saveTxt(datalist, savepath):
    print("save txt.......")
    txtfile = open(savepath, 'w', encoding='utf-8')
    
    for i in range(0, len(datalist)):
        txtfile.write(datalist[i][2]+"（"+datalist[i][1]+"）\n")
        txtfile.write("别名：\n")
        txtfile.write("CV："+datalist[i][4]+datalist[i][3]+"\n")
        txtfile.write("CV介绍：\n\n")
    txtfile.close()

# main函数
if __name__ == "__main__":
    
    # 1.爬取网页+解析数据
    datalist = getData(url)

    print("爬取完毕！")
    
    # 2.当前目录创建XLS，保存数据
    saveData(datalist, gamename+".xls")
    
    # 3.当前目录创建TXT，保存数据
    saveTxt(datalist, gamename+".txt")

    print("输出完毕！")