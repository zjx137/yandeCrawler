__author__ = 'Bacbin'

import crawler
import time
from multiprocessing import Pool
#文件路径，如文件夹不存在会自动创建，请务必拼对单词
u_folder_apth = "/Users/bacbin/Desktop/程序设计/py-crawler/brabra"
#默认url
url = 'https://yande.re/post?tags='
#tags = 'azur_lane'


def CoreProcess(tags, from_page, end_page):    
    arr = crawler.getUrlList(url,tags,from_page,end_page)
    downloadList = []
    print('开始收集图片下载地址...')
    for i in range(len(arr)):
        downloadList.append(crawler.getImgUrl(arr[i]))
    crawler.downloadImg_Pool(u_folder_apth,downloadList)
    print('下载完成!')

def main():
    tags = input('请输入Tags:')
    from_num = int(input('开始页面：'))
    from_page = from_num if from_num > 0 else 1 
    end_num = int(input('结束页面：'))
    end_page = end_num if end_num > from_page else from_page
    start = time.time()
    CoreProcess(tags, from_page, end_page)
    #print(end_page)
    end = time.time()
    print('用时: ',int(end-start))


if __name__ == '__main__':
    main()
