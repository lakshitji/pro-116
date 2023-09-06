import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(100,100),cv2.FONT_ITALIC,fontScale=1.5,color=(0,0,255))
cv2.putText(img,"Mercury",(120,180),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(195,265),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(292,265),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(380,260),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(580,50),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(750,100),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(980,130),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1125,130),cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)