import cv2
from mtcnn import MTCNN
import json

detector = MTCNN()

image = cv2.cvtColor(cv2.imread("1.jpg"), cv2.COLOR_BGR2RGB)
result = detector.detect_faces(image)

# Result is an array with all the bounding boxes detected.
j=0
num_of_faces = len(result)
boxes = {}
for i in range(0,num_of_faces):
    bounding_box = result[i]['box']
    boxes["face_{}".format(j+1)] = bounding_box
    tempim = image[bounding_box[1]:(bounding_box[1] + bounding_box[3]), bounding_box[0]:(bounding_box[0] + bounding_box[2])]
    cv2.imwrite("face_{}.jpg".format(j+1), cv2.cvtColor(tempim, cv2.COLOR_RGB2BGR))
    j=j+1

with open("boxes.json", "w") as boxes_file:
    json.dump(boxes, boxes_file, indent = 4)

print("Number of faces detected: ", num_of_faces)
