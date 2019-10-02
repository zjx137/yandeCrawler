from bs4 import BeautifulSoup
import requests
import urllib
import re
import os

def getHtml(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    html = req.text
    return html

def getUrlList(url, tags,fromPage,endPage):
    init_url = url + tags
    url_list = []
    #page_n = '&page='+page_number
    for i in range(fromPage,endPage+1):
        url_list.append(init_url+'&page='+str(i))
    arr = []
    print('开始收集图片URL...')
    for url in url_list:
        html = getHtml(url)
        soup = BeautifulSoup(html, "lxml")
        res = soup.find_all(id='post-list-posts')[0].find_all("a",class_ = "thumb")
        for items in res:
            arr.append('https://yande.re'+items['href'])
    return arr

def getImgUrl(url):
    html = getHtml(url)
    soup = BeautifulSoup(html,"lxml")
    res = soup.find(id='right-col').find("img",class_='image')
    return res['src']
    
def downloadImg(folder_path, lists):
    if not os.path.exists(folder_path):
        print("选定的文件夹不存在，帮你先创一个。")
        os.makedirs(folder_path)
    for url in lists:
        print("正在下载Pic: {}".format(url))
        filename = url.split('/')[-1]
        filepath = folder_path + '/' + filename
        if os.path.exists(filepath):
            print("文件已存在 ，咱换！！")
        else:
            try:
                urllib.request.urlretrieve(url, filename=filepath, reporthook=Schedule)
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)


def Schedule(blocknum,blocksize,totalsize):
    '''''
     blocknum:已经下载的数据块
     blocksize:数据块的大小
     totalsize:远程文件的大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per>100:
        per = 100
    print('当前下载进度：%d'%per)