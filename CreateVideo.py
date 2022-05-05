import os
import cv2

path = "Images/"

images = []

for file in os.listdir(path):
    os.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','jfif']:
        file_name = path + '/' + file
        print(file_name)
    images.append()

    count = len(images)
    frame = cv2.imread(images[0])

    height = int(cv2.CAP_PROP_FRAME_HEIGHT)
    width = int(cv2.CAP_PROP_FRAME_WIDTH)

    size = (width,height)
    print(size)

    out = cv2.VideoWriter('project_av1',cv2.Video_Writer_fourcc(*'DIVX'),0.8,size)

    for i in range(0,count-1):
        cv2.imread()
        out.write()
        print("Done")
