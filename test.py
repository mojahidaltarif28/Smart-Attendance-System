import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change

img = cv2.imread(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\report.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3))) 

cv2.imshow("Deteced-face",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()