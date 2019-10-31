# yandeCrawler
> yande.re爬虫

主要是通过tags标签查找下载，按理说通过其他的标签也行，只需修改一下URL中queryParams

可以多页连续下载，也可单页下载

## 使用方法
> 使用前请务必更改`main.py`中的u_folder_path为所要下载到本地的文件夹路径

Mac

```python
python3 main.py
```

Windows

双击main.py

## 需求
- python 3.4
- BeautifulSoup
- multithreading
```python
pip3 install Beautifulsoup4 
```
