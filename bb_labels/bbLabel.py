"""
    Expects box.json and info.json along with the original Image
    Puts up text according to the labels while color coding it 
    according to the score.
"""
from cv2 import cv2
import json

img_path = "1.jpg"
boxes_path = "boxes.json"
info_path = "info.json"


img = cv2.imread(img_path)
boxes = json.load(open(boxes_path, "r"))

info = json.load(open(info_path, "r"))

for face in boxes.keys():
    box = boxes[face]
    details = info[face]
    name = details[0]
    score = details[1]

    if (score>0.7):
        color = (0,255,0)
    elif (score<0.3):
        color = (0,0,255)
    else:
        color = (0,255,255)
    
    cv2.putText(img,
            name,
            (box[0], box[1]-5),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.7,
            color,
            1)

    img1 = cv2.rectangle(img,
                        (box[0], box[1]),                       # top left 
                        (box[0] + box[2], box[1] + box[3]),     # bottom right
                        color,
                        2)                                      # thickness

cv2.imshow("Boxed Image", img1)
cv2.waitKey(0)