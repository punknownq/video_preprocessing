# 导入cv2模块
import cv2
import os
from os.path import basename

folder_pic = "pic-10"
filepath = "video"
pathDir = os.listdir(filepath)
i = 0
for allDir in pathDir:
    #name = "CameraID-3-Time-2013.11.03-12.05.46 -1"
    cap = cv2.VideoCapture(os.path.join('video',allDir))  # 要分解的视频的路径

    if cap.isOpened():
        flag = 1
    else:
        flag = 0


    c = 1
    timeF = 10

    if flag == 1:
        folder = os.path.exists(folder_pic)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(folder_pic)
        while True:
            ret, frame = cap.read()  # 读取视频帧
            if ret == False:  # 判断是否读取成功
                break
            if(c%timeF == 0):
                imgPath = os.path.join(folder_pic,basename(allDir)+'-%s.png')% str(i)
                #imgPath = "CameraID-3-Time-2012-04-24-16-45-15/%s.jpg" % str(i)  # 存储图片的路径
                cv2.imwrite(imgPath, frame)  # 将提取的视频帧存储进imgPath
                i += 1  # 使用i为图片命名
            c += 1
print("finish!")  # 提取结束，打印finish
