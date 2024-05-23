from bs4 import BeautifulSoup


# 示例 HTML 字符串
html_content = '''
<span class="number" property="v:average">9.3</span>
<span class="number" property="v:average">9.2</span>
<a href="/subject/326" class="l">攻壳机动队 S.A.C. 2nd GIG</a>
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'lxml')

# 查找第一个特定的 span 元素
span_element = soup.find('span', class_='number', property='v:average')

# 提取文本内容
if span_element:
    number = span_element.text
    print(number)  # 输出: 9.2
else:
    print("没有找到匹配的元素")

print()

# 查找所有特定的 span 元素
span_elements = soup.find_all('span', class_='number', property='v:average')

# 提取文本内容
if span_elements:
    for span_element in span_elements:
        number = span_element.text
        print(number)  # 输出: 9.2
else:
    print("没有找到匹配的元素")


# 查找第一个特定的 span 元素
span_element = soup.find('a', class_='l')

# 提取文本内容
if span_element:
    number = span_element.text
    print(number)  # 输出: 9.2
else:
    print("没有找到匹配的元素")

print()