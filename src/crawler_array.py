#支援多關鍵字爬圖

import icrawler_image
import threading


def run_crawler_image_thread(keyword_list,imgNum):
	for item in keyword_list:
		dirpath = icrawler_image.createDir(item)
		threading.Thread(target = icrawler_image.getImg, args = (item, dirpath, imgNum), name = 'thread-' + str(item) ).start()

def run_crawker_image_for(keyword_list,imgNum):
	# threads = []
	# thread_num = 0
	# for item in keyword_list:
	# 	thread_num += 1
	# 	dirpath = icrawler_image.createDir(item)
	# 	threads.append(threading.Thread(target = icrawler_image.getImg, args = (item, dirpath, imgNum), name = 'thread-' + thread_num ))
	for item in keyword_list:
		dirpath = icrawler_image.createDir(item)
		icrawler_image.getImg(item, dirpath, imgNum)

if __name__ == '__main__':
	try:
		keyword_list = input("Please input keyword list:(ex: keyoword1,keyowrd2,...)\n")
		keyword_list = keyword_list.split(',')
		imgNum = int(input("How many images?\n"))
		run_crawler_image_thread(keyword_list,imgNum)
		# run_crawker_image_for(keyword_list,imgNum)
	except ValueError:
		print("It's not a number! \n")
	except Exception as e:
		print(e)
	