import csv
from bs4 import BeautifulSoup
import requests


def request(url):
    '''请求网页数据'''

    # 设置请求头部信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.content.decode("utf-8")
            return html
        else:
            print(f'Request failed with status code: {response.status_code}')
    except requests.RequestException as e:
        print(f'An error occurred: {e}')


def find_data(html):
    '''解析网页数据'''
    return BeautifulSoup(html, "html.parser")


def get_name(soup):
    '''获取作品名'''
    names = soup.find_all('a', class_='l')
    names = [name for name in names if name['href'].startswith('/subject/')]
    return names


def get_grade(soup):
    '''获取评分'''
    grades = soup.find_all('small', class_='fade')
    # grades = [grade for grade in grades if grade['href'].startswith('/subject/')]
    return grades


def get_vote(soup):
    '''获取评分人数'''
    votes = soup.find_all('span', class_='tip_j')
    return votes


def save_data(names, grades, votes, option='a', flag = 1):
    '''保存数据'''
    with open('gradevsvotes.csv', option, encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if flag == 0:
            writer.writerow(('Name', 'Grade', 'Votes'))
        for i in range(len(names)):
            writer.writerow((names[i].text, grades[i].text, votes[i].text))


if __name__ == "__main__":
    baseurl = "https://bgm.tv/"

    for page in range(1, 50):
        url = baseurl + "anime/browser?sort=rank&page=" + str(page)
    
        response = request(url)
        soup = find_data(response)

        names = get_name(soup)
        grades = get_grade(soup)
        votes = get_vote(soup)

        for name in names:
            print(name.text)

        if page == 1:
            save_data(names, grades, votes, 'w', 0)
        else:
            save_data(names, grades, votes)