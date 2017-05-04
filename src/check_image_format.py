#移除非圖片格式之檔案
import os
				
def check_extension(dirPath):
	fileDir = dirPath
	for root, dirs, files in os.walk(fileDir):
		for dirp in dirs:
			print(dirp)
			folder = fileDir+"\\"+dirp
			command = "rmdir /s /q %s"
			command = command % folder
			result = os.system(command)
			if result == 0:
				print ("delete success")
			else:
				print ("delete fail")

		for file in files:
			try:
				att = os.path.splitext(fileDir+"\\"+file)[-1]
				if att!='.jpg' and att!='.JPG' and att!='.jpeg' and att!='.gif' and att!='.png':
					if att[0:4]=='.jpg':
						print (os.path.splitext(fileDir+"\\"+file)[0]+att[0:4])
						print (fileDir+"\\"+file)
						old_name = fileDir+"\\"+file
						new_name = os.path.splitext(fileDir+"\\"+file)[0]+att[0:4]
						os.renames(old_name,new_name)
					
					print(file)
					os.remove(fileDir+"\\"+file)
					print(att)
			except Exception as e:
				continue

if __name__ == '__main__':
	nowDirectory = os.getcwd()
	for tops, dirs, files in os.walk(nowDirectory):
		for dir in dirs:
			check_extension(os.path.join(tops,dir))

