# 名稱:		icrawler_image
# 開發者:	kimi_tsai@2017/03/14
# 說明:		google, bing, baidu 爬圖

import os
import time
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

def kimi():
	print("kimi")

def createDir(name):
	# print(time.strftime("%H_%M_%S"))
	dir_name = name + "_" +time.strftime("%Y%m%d_%H_%M_%S")
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
	return dir_name

def getImg(keyword="5566", dirpath="", imgNum=10):
	print("keyword:" + keyword +", images:"+ str(imgNum) +"\n\n")

	google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': dirpath})
	google_crawler.crawl(keyword=keyword, offset=0, max_num=imgNum,date_min=None, date_max=None, min_size=(200, 200), max_size=None)

	bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': dirpath})
	bing_crawler.crawl(keyword=keyword, offset=0, max_num=imgNum, min_size=None, max_size=None)

	baidu_crawler = BaiduImageCrawler(storage={'root_dir': dirpath})
	baidu_crawler.crawl(keyword=keyword, offset=0, max_num=imgNum,min_size=None, max_size=None)


def main():
	mykeyword = input("Please input keyword:\n")
	# mykeyword = "5566"

	imgNum = int(input("How many images?\n"))
	# imgNum = 1

	dirpath = createDir(mykeyword)
	getImg(mykeyword,dirpath,imgNum)

if __name__ == '__main__':
	main()