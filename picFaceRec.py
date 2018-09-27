# -*- coding: UTF-8 -*-
import face_recognition
import cv2
import os
import shutil

# 加載示例圖片並學習如何識別它。
path ="images"#在同級目錄下的images文檔中放需要被識別出的人物圖
total_image=[]
total_image_name=[]
total_face_encoding=[]
for dn in os.listdir(path): #dn表示的是資料夾名
  dn_name = dn[:(len(dn))]#截取圖片名（這裏應該把images文檔中的資料夾名命名為為人物名）
  for fn in os.listdir(path+"/"+dn):
    total_face_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(path+"/"+dn+"/"+fn))[0])
    total_image_name.append(dn_name)#名字列表

#跑遍picture資料夾裡所有的照片
for pic in os.listdir("pictures"):
	frame = cv2.imread("pictures/"+pic)
	print(pic)
	find = 0
	# 發現在照片所有的臉和face_enqcodings
	face_locations = face_recognition.face_locations(frame)
	face_encodings = face_recognition.face_encodings(frame, face_locations)
	#在這個視頻幀中循環遍歷每個人臉
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		# 看看面部是否與已知人臉相匹配。
		for i,v in enumerate(total_face_encoding):
			match = face_recognition.compare_faces([v], face_encoding,tolerance=0.5)
			name = "Unknown"
			if match[0]:
				name = total_image_name[i]
				find = 1
				break
	if find == 1:
		shutil.copy("pictures/"+pic,"wanted_pictures")
		#print(pic)
	#顯示結果圖像
 	#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
 	#cv2.imshow('image', frame)
 	#cv2.waitKey(0)
 	#cv2.destroyAllWindows()

