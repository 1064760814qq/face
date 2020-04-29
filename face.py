# #1.导入库
import cv2

import pandas
# #2 加载图片
# image = cv2.imread('C:/Users/10647/Desktop/demo1/timg (1).jfif')
# #3 加载人脸模型
# cv2.CascadeClassifier
# #4 调整图片灰度
#
# #5 检查人脸
# #6 标记人脸
#
# #7 创建窗口
#
# #8 暂停窗口
#
# #9 关闭窗口

#导入图片
img = cv2.imread('C:/Users/Administrator/Desktop/demo1/timg (4).jfif', 1)
#加载人脸模型库
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#识别人脸
faces = face_engine.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
#标记人脸
for (x, y, w, b) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + b), (255, 255, 0), 2) #
cv2.namedWindow('test windows')
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

