from cvlib.object_detection import YOLO
import cv2
from esp32tst import cam
weights="yolov3.weights"
config="yolov3.cfg"
labels="coco.names"
#img=cv2.imread("img.jpg")
while True:
    img=cam()
    img=cv2.resize(img,(680,460))
#    yolo = YOLO(weights, config,labels)
#    bbox, label, conf = yolo.detect_objects(img)
#    img1=yolo.draw_bbox(img, bbox, label, conf)
    cv2.imshow("img1",img)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.destroyAllWindows()    
